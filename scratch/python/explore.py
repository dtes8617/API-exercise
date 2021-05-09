import os
import dotenv

from twilio.rest import Client

dotenv.load_dotenv()


class Messenger:
    def __init__(self):
        self.client = Client(username=os.getenv("TWILIO_ACCOUNT_SID"), password=os.getenv("TWILIO_AUTH_TOKEN"))

    def get_all_message(self):
        for msg in self.client.messages.list():
            print(msg.body)

    def send_message(self, to_number=os.getenv("MY_NUMBER"), content: str = ''):
        msg = self.client.messages.create(
            to=to_number,
            from_=os.getenv("TWILIO_NUMBER"),
            body=content
        )
        print(f"Created a new message: {msg.sid}")

    def delete_messages(self):
        for msg in self.client.messages.list():
            print(f'Deleting {msg.body}')
            msg.delete()


if __name__ == "__main__":
    messenger = Messenger()
    # messenger.get_all_message()
    # messenger.send_message(content="Hello from Python")
    messenger.delete_messages()