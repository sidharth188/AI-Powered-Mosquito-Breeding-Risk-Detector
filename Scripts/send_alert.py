from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

def send_whatsapp(risk_level, image_path):
    client = Client(os.getenv("TWILIO_SID"), os.getenv("TWILIO_AUTH"))
    body = f"⚠️ Alert: A mosquito breeding hotspot has been detected.\n\nRisk Level: {risk_level}\nImage: {image_path}"
    
    message = client.messages.create(
        from_=os.getenv("WHATSAPP_FROM"),
        body=body,
        to=os.getenv("WHATSAPP_TO")
    )
    print("Message sent:", message.sid)
