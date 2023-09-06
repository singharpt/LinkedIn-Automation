from send_emails import send_emails
from get_attachments import get_attachments
from get_comments import get_emails_from_comments
from manage_cache import Cache

# get all emails from the linkedIn comment section
try:
    print("Getting emails from linkedIn comments box...")
    email_list = get_emails_from_comments()
except:
    email_list = []
    print(f"Error getting emails from LinkedIn")

# send the emails only when emails found
if email_list:

    # run cache check to make sure no duplicate are send to seen emails
    cache = Cache()
    unseen_email_list = cache.run_cache_check(email_list)

    # if unseen emails are present
    if unseen_email_list:

        print("Sending bulk emails...")

        # get the attachments
        attachment_list = get_attachments()

        response = send_emails(unseen_email_list, attachment_list)

        if response['status']:
            print("Emails sent :)")
            cache.update_cache(unseen_email_list)
        else:
            print(f"Error in sending emails :({response['message']}")

    else:
        print("No new emails received...")
