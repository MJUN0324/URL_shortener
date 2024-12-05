import json
import os
import boto3

# Initialize AWS clients
tableName = os.environ.get("URLSHORTNERTABLE_TABLE_NAME")
dynamodb = boto3.resource("dynamodb")

# Environment variables
table = dynamodb.Table(tableName)


def handler(event, context):
    try:
        # delete/{id}
        recordId = event["pathParameters"]["id"]

        # delete matching id
        response = table.delete_item(Key={"id": recordId})
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "Record deleted successfully"}),
            "headers": {"Content-Type": "application/json"},
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 404,
            "body": json.dumps({"message": str(e)}),
            "headers": {"Content-Type": "application/json"},
        }
