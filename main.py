from send_emails import send_emails
from get_attachments import get_attachments
from get_comments import get_emails_from_comments

# get all emails from the linkedIn comment section
try:
    print("Getting emails from linkedIn comments box...")
    email_list = get_emails_from_comments()
except:
    email_list = []
    print(f"Error getting emails from LinkedIn")

# send the emails only when emails found
if email_list:

    print("Sending bulk emails...")

    # get the attachments
    attachment_list = get_attachments()

    response = send_emails(email_list, attachment_list)

    if response['status']:
        print("Emails sent :)")
    else:
        print(f"Error in sending emails :({response['message']}")
