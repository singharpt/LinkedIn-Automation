from __future__ import print_function
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
import os
from dotenv.main import load_dotenv
load_dotenv()

configuration = sib_api_v3_sdk.Configuration()

# get the envionment variables
configuration.api_key['api-key'] = os.environ['API_KEY']
sender_email = os.environ['SENDER_EMAIL']
sender_name = os.environ['SENDER_NAME']
email_subject = os.environ['EMAIL_SUBJECT']
email_body_text = os.environ['EMAIL_TEXT']
email_body_html = os.environ['EMAIL_HTML']


def send_emails(email_list, attachment_list):
    """
    This is an implementation of the brevo <sendInBlue> API. Docs: https://developers.brevo.com/docs/how-it-works
    Input: List of dictionary <emails>, List of dictionary <attachments>
    Output: API Response
    """
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(
        sib_api_v3_sdk.ApiClient(configuration))
    subject = email_subject
    sender = {"name": sender_name, "email": sender_email}
    html_content = email_body_text
    to = email_list
    attachments = attachment_list
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=to, text_content=email_body_text, html_content=html_content, sender=sender, subject=subject, attachment=attachments)

    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        return {'status': True, 'message': api_response}
    except ApiException as e:
        return {'status': False, 'message': f"Exception when calling SMTPApi->send_transac_email: {e}"}
