# Import necessary libraries
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv(dotenv_path="/Volumes/Workstation/Learning Center/Data Science/"
                        "100 Days of Code - Complete Python Pro Bootcamp 2021/Projects/@CREDENTIALS/.env")
# Constants
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = "whatsapp:+14155238886"
RECEIVER = "whatsapp:+8801701340839"


class NotificationManager:
    def __init__(self):
        self.SID = TWILIO_SID
        self.AUTH_TOKEN = TWILIO_AUTH_TOKEN

    def send_message(self, price: str, dep_city: str, dep_ap_iata_code: str, arr_city: str,
                     arr_ap_iata_code: str,outbound_date: str, inbound_date: str):
        client = Client(self.SID, self.AUTH_TOKEN)
        message = client.messages.create(
            body=f"Low price alert! Only ${price} to fly from {dep_city}-{dep_ap_iata_code}"
                 f" to {arr_city}-{arr_ap_iata_code}, from {outbound_date} to {inbound_date}.",
            from_=TWILIO_PHONE_NUMBER,
            to=RECEIVER
        )
        print(message.sid)
