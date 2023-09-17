# LinkedIn Data Sharing Automation Tool

## Overview

This tool automates the process of sharing data with LinkedIn users who request it through posts. It eliminates the need to manually collect email addresses and send data, making the process efficient and privacy-focused.

## Key Features

- **Privacy-Focused:** Your data stays private; no need to share personal information with third-party websites.
- **Cost-Free:** Completely free to use, saving you money and simplifying data sharing.
- **Scheduled Execution:** Set it to run automatically daily, weekly, monthly, or as needed.
- **Email Tracking:** Prevents duplicate emails and maintains a record of sent emails.
- **Attachment Support:** Attach various file types, such as images, PDFs, documents, and more.
- **Seamless Execution:** Runs in the background without disrupting your tasks.

## How It Works

1. **LinkedIn Data Extraction:** It logs into your LinkedIn account using Selenium and extracts email addresses from post comments.
2. **Cache Check:** Filters out unique email addresses and prevents duplicates using cache data.
3. **Attachment Preparation:** Converts files from a specified folder into email attachments.
4. **Bulk Email Sending:** Uses the Brevo transactional email API to send emails in bulk.
5. **Cache Update:** Updates the cache.txt file with newly sent email addresses.

## How to Use

1. **Clone Repository:** Clone this repository using [this link](https://github.com/singharpt/LinkedIn-Automation.git).
2. **Create Brevo API Account:** Visit [Brevo API](https://onboarding.brevo.com/account/register) and complete the registration process.
3. **Choose the Free Plan:** Select the free tier plan, providing 300 free emails per day.
4. **Generate API Keys:** Go to [API Key Generation](https://app.brevo.com/settings/keys/api), create a new API key, and save it in a text file for later use.
5. **Update .env File:**
   - Open the .env file in the cloned folder and update the following values:
     - `API_KEY`: Paste the Brevo API key.
     - `SENDER_EMAIL`: Your Brevo account email (e.g., arpit.singh@utdallas.edu).
     - `SENDER_NAME`: Your name associated with the email.
     - `POST_URL`: URL of your LinkedIn post.
     - `LINKEDIN_EMAIL`: Your LinkedIn username/email.
     - `LINKEDIN_PASSWORD`: Your LinkedIn password (The tool runs locally, ensuring data privacy).
     - `EMAIL_SUBJECT`: Subject of the email you want to send.
     - `EMAIL_TEXT`: Email body.
     - `EMAIL_HTML`: Optional HTML content (leave empty if not needed).
     - `EMAIL_ATTACHMENT_FOLDER_PATH`: Path to the folder containing attachments (e.g., /Users/Documents/Attachments).

## Tech Stack

- Python
- Object-Oriented Programming
- Selenium
- Brevo SendInBlue Email API
- CronJobs (Linux/MacOS)

## Contributions

Contributions and improvements are welcome. Feel free to open an issue to discuss new features, bug fixes, or enhancements.

Please note that this project was experimental and intended for learning purposes. There may be room for better and optimized solutions to the same problem.

If you encounter issues or have questions, contact me directly at [arpit.singh@utdallas.edu](mailto:arpit.singh@utdallas.edu).

## Acknowledgments

Thanks to the open-source community for their contributions and support in developing this tool.
