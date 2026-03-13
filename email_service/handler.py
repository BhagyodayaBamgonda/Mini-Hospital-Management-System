import json

def send_email(event, context):

    print("EMAIL SERVICE TRIGGERED")

    body = json.loads(event["body"])
    action = body.get("action")

    if action == "BOOKING_CONFIRMATION":
        print("Booking confirmation email triggered")

    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Email sent"})
    }