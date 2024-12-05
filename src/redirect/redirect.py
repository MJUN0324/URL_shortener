import json
import os
import boto3
import time
from boto3.dynamodb.conditions import Key

# Initialize AWS clients
tableName = os.environ.get("URLSHORTNERTABLE_TABLE_NAME")
dynamodb = boto3.resource("dynamodb")

# Environment variables
table = dynamodb.Table(tableName)


def handler(event, context):
    try:
        shortCode = event["pathParameters"]["shortCode"]
        response = table.query(
            IndexName="url_index",
            KeyConditionExpression=Key("shortCode").eq(shortCode),
            # ExpressionAttributeValues={":shortCode": shortCode},
        )
        print(f"{response}")
        items = response.get("Items", [])
        print(items)

        if items:
            item = items[0]
            # get individual key
            originalUrl = item["originalUrl"]
            primaryKey = {"id": item.get("id")}
            expiredAt = int(time.time()) + 600

            # increment number of clicks, each time a url is visited
            table.update_item(
                Key=primaryKey,
                UpdateExpression="SET expiredAt=:e ADD clicks :increment ",
                ExpressionAttributeValues={":increment": 1, ":e": expiredAt},
                ReturnValues="UPDATED_NEW",
            )

        return {
            "statusCode": 302,
            "body": json.dumps({"message": "Redirecting to the original URL"}),
            "headers": {
                "Content-Type": "application/json",
                "Location": originalUrl,
            },
        }

    except Exception as e:
        print(e)
        return {
            "statusCode": 404,
            "body": "No Matching URL",
            "headers": {"Content-Type": "application/json"},
        }
