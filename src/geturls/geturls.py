import json
import boto3
import os
from decimal import Decimal

# Initialize AWS clients
tableName = os.environ.get("URLSHORTNERTABLE_TABLE_NAME")
dynamodb = boto3.resource("dynamodb")

# Environment variables
table = dynamodb.Table(tableName)


# Convert Decimal to int for JSON serialization
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return int(obj)
    raise TypeError


def handler(event, context):
    try:
        response = table.scan()
        items = response["Items"]

        # extract specific fields
        filteredItems = [
            {
                "id": item["id"],
                "shortCode": item["shortCode"],
                "createdAt": item["createdAt"],
                "originalUrl": item["originalUrl"],
                "shortUrl": item["shortUrl"],
            }
            for item in items
        ]
        return {
            "statusCode": 200,
            "body": json.dumps(filteredItems, default=decimal_default),
            "headers": {"Content-Type": "application/json"},
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 404,
            "body": json.dumps({"message": str(e)}),
            "headers": {"Content-Type": "application/json"},
        }
