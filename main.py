from send_emails import send_emails
from get_attachments import get_attachments
from get_comments import get_emails_from_comments

# get all emails from the linkedIn comment section
# email_list = get_emails_from_comments()

email_list = [{'Email': 'arpitsingh.97@icloud.com'}]

# get the attachments
attachment_list = get_attachments()

# send the emails
response = send_emails(email_list, attachment_list)

# print response
print(response)
