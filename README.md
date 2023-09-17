# Automated LinkedIn Data Sharing Tool

## Overview

LinkedIn users often create posts to share data publicly, requesting interested users to comment with their email addresses. These posts can receive an overwhelming response, sometimes exceeding 1000+ interested users. To address this challenge, I have developed an in-house solution that automates the process of sending requested data to interested users.

## Key Features

- **Privacy-Focused:** Unlike other online solutions, my tool doesn't require you to share your personal data with a website, ensuring your privacy.
- **Cost-Free:** My solution is completely free to use, saving you money while simplifying the data sharing process.
- **Auto scheduling:** You can schedule it to run automatically on a particular time every-day, every-week, every-month, every-year, etc.
- **Keeps track of emails sent:** The solution ensures that duplicate emails are not sent to the same user and provides a list of all emails mailed till the last run.
- **Supports various email attachments:** You can attach single or multiple attachments. Supports all major attachments including images, pdfs, docs, excel, csv, etc.
- **Runs seamlessly:** The solution runs seamlessly in the background and does not hinder the task user might be performing at the moment.

## How it works

1. **Gets LinkedIn data using Selenium:** Logs into user's LinkedIn account using Selenium, and gets the comments' section data of the target post.
2. **Checks the cache:** After extracting all email addresses present in the comments section it filters out all unique emails using the cache data.
3. **Gets the attachments ready:** Goes to the target folder specified by the user and converts all the files as binary data to be attached with the email.
4. **Send bulk email:** Using the Brevo transactional email API, bulk emails are sent to the users.
5. **Updates the cache:** Once emails are delivered to the target email addresses, it updates the cache.txt file (inside the project directory) with the new email addresses.

## How to use

1. **Clone Repo:** Clone Repository: Clone this repo using this link - [GitHub Repo](https://github.com/singharpt/LinkedIn-Automation.git).
2. **Create Account at Brevo API:** Go to [Brevo API](https://onboarding.brevo.com/account/register) and fill in your details.
3. **Select the FREE plan:** Select the free tier plan, which provides you with 300 emails a day for free.
4. **Create API Keys:** Go to [Brevo API Key Generation](https://app.brevo.com/settings/keys/api), click on "Generate a New API Key," give it a name, and click on generate. MOST IMPORTANT: copy the API key to a text file, we will need it later.
5. **Update .env file:**
   - Go to the folder you just cloned from the GitHub and open the .env file. Update the key values as per the instructions below:
   - `API_KEY`: Paste the Brevo API key value we just got from the Brevo API Website.
   - `SENDER_EMAIL`: Enter the email address you used to create an account at Brevo. For example, arpit.singh@utdallas.edu
   - `SENDER_NAME`: Enter the name associated with the above email address
   - `POST_URL`: Enter the URL of your post on LinkedIn
   - `LINKEDIN_EMAIL`: Enter your LinkedIn username/email
   - `LINKEDIN_PASSWORD`: Enter your LinkedIn password (Don't worry! The solution works locally on your PC; your data will not be shared with anyone)
   - `EMAIL_SUBJECT`: Enter the subject of the email you want to send (For example, Hi! I got the data you requested in the LinkedIn comment section)
   - `EMAIL_TEXT`: Enter the body of your email.
   - `EMAIL_HTML`: In case you want to add any HTML content, you can; otherwise, you can leave this empty. (DO NOT DELETE THE KEY)
   - `EMAIL_ATTACHMENT_FOLDER_PATH`: This is the path to your folder that contains all the attachments. For example, /Users/Documents/Attachments

## Tech Stack Used

- Python
- Object-Oriented Programming
- Selenium
- Brevo SendInBlue Email API
- CronJobs (Linux/MacOS)

## Contributions

Contributions and improvements to this project are welcome. Please open an issue to discuss any new features, bug fixes, or enhancements you'd like to contribute.

Please note that this was an experimental project only for learning purposes. I believe a better and optimized solution for the specific problem could be developed.

If you encounter any issues or have questions, please feel free to contact me directly at [arpit.singh@utdallas.edu](mailto:arpit.singh@utdallas.edu).

## Acknowledgments

I'd like to thank the open-source community for their contributions and support in developing this tool.
