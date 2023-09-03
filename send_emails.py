from mailjet_rest import Client
from dotenv.main import load_dotenv
import os
load_dotenv()

# get the envionment variables
api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET_KEY']
sender_email = os.environ['SENDER_EMAIL']
sender_name = os.environ['SENDER_NAME']
email_subject = os.environ['EMAIL_SUBJECT']
email_body_text = os.environ['EMAIL_TEXT']
email_body_html = os.environ['EMAIL_HTML']


def send_emails(emails, attachments):
    """
    This is an implementation of the mailJet API. Docs: https://dev.mailjet.com/email/guides/
    Input: List of dictionary <emails>
    Output: API Response
    """
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
                "From": {
                    "Email": sender_email,
                    "Name": sender_name
                },
                "To": emails,
                "Subject": email_subject,
                "TextPart": email_body_text,
                "HTMLPart": email_body_html,
                "Attachments": attachments
            }
        ]
    }

    result = mailjet.send.create(data=data)
    return result.json()
