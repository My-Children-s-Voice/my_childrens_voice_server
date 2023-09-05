from firebase_admin import messaging

def send_message(token: str, title:str, body: str):
    message = messaging.Message(
    notification = messaging.Notification(
            title=title,
            body=body
        ),
        token=token,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)