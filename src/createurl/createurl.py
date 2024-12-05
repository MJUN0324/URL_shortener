import json
import os
import time
import boto3
import uuid
import random
import string
from datetime import datetime, timedelta

# Initialize AWS clients
tableName = os.environ.get("URLSHORTNERTABLE_TABLE_NAME")
dynamodb = boto3.resource("dynamodb")

# Environment variables
table = dynamodb.Table(tableName)


def generate_short_code(url, length=5):
    char_pool = string.ascii_uppercase + string.ascii_letters + string.digits
    return "".join(random.sample(char_pool, length))


def handler(event, context):
    print(event)
    body = json.loads(event["body"])
    print(f"Body from event: {body}")

    originalUrl = body.get("originalUrl")
    shortCode = body.get("shortCode")

    stage = event["requestContext"]["stage"]
    if not originalUrl:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Url is required"}),
        }

    if not shortCode:
        shortUrlResponse = generate_short_code(originalUrl)
    else:
        shortUrlResponse = shortCode

        # if stage == "dev":
        #     print("match")
        #     shortUrl = f"https://{event['headers']['host']}/{stage}/{shortUrlResponse}"
        # else:
        #     print("custom domain")
        shortUrl = f"https://{event['headers']['host']}/{shortUrlResponse}"

    expiredAt = int(time.time()) + 600  # 10 minutes in seconds
    data = {
        "id": str(uuid.uuid4()),
        "originalUrl": originalUrl,
        "shortCode": shortUrlResponse,
        "createdAt": datetime.now().isoformat(),
        "clicks": 0,
        "shortUrl": shortUrl,
        "expiredAt": expiredAt,
    }
    try:
        table.put_item(Item=data)
        return {
            "statusCode": 201,
            "body": json.dumps({"shortUrl": shortUrl}),
            "headers": {"Content-Type": "application/json"},
        }
    except Exception as e:
        response = {
            "statusCode": 403,
            "body": json.dumps({"message": "error saving data"}),
        }
