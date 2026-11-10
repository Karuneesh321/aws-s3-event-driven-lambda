import json
import urllib.parse
from datetime import datetime, timezone

def lambda_handler(event, context):

    print("================================")
    print("S3 EVENT AUTOMATION STARTED")
    print("================================")

    for record in event.get("Records", []):

        bucket_name = record["s3"]["bucket"]["name"]

        object_key = urllib.parse.unquote_plus(
            record["s3"]["object"]["key"]
        )

        object_size = record["s3"]["object"].get("size", 0)

        event_name = record.get("eventName", "Unknown")

        event_time = record.get("eventTime", "Unknown")

        print("Event Details:")
        print("Bucket:", bucket_name)
        print("File Name:", object_key)
        print("File Size:", object_size, "bytes")
        print("Event Type:", event_name)
        print("Event Time:", event_time)

        print("File upload detected successfully!")

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "S3 event processed successfully"
        })
    }