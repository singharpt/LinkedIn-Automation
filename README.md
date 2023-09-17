<!DOCTYPE html>
<html>

<head>
    <title>Automated LinkedIn Data Sharing Tool</title>
</head>

<body>

    <h1>Automated LinkedIn Data Sharing Tool</h1>

    <section>
        <h2>Overview</h2>
        <p>LinkedIn users often create posts to share data publicly, requesting interested users to comment with their email addresses. These posts can receive an overwhelming response, sometimes exceeding 1000+ interested users. To address this challenge, I have developed an in-house solution that automates the process of sending requested data to interested users.</p>
    </section>

    <section>
        <h2>Key Features</h2>
        <ul>
            <li><strong>Privacy-Focused:</strong> Unlike other online solutions, my tool doesn't require you to share your personal data with a website, ensuring your privacy.</li>
            <li><strong>Cost-Free:</strong> My solution is completely free to use, saving you money while simplifying the data sharing process.</li>
            <li><strong>Auto scheduling:</strong> You can schedule it to run automatically on a particular time every-day, every-week, every-month, every-year, etc.</li>
            <li><strong>Keeps track of emails sent:</strong> The solution ensures that duplicate emails are not sent to the same user and provides a list of all emails mailed till the last run.</li>
            <li><strong>Supports various email attachments:</strong> You can attach single or multiple attachments. Supports all major attachments including images, pdfs, docs, excel, csv, etc.</li>
            <li><strong>Runs seamlessly:</strong> The solution runs seamlessly in the background and does not hinder the task the user might be performing at the moment.</li>
        </ul>
    </section>

    <section>
        <h2>How it works</h2>
        <ol>
            <li><strong>Gets LinkedIn data using selenium</strong> Logs into user's LinkedIn account using Selenium and gets the comments' section data of the target post.</li>
            <li><strong>Checks the cache:</strong> After extracting all email addresses present in the comments section, it filters out all unique emails using the cache data.</li>
            <li><strong>Gets the attachments ready:</strong> Goes to the target folder specified by the user and converts all the files as binary data to be attached with the email.</li>
            <li><strong>Send bulk email:</strong> Using the Brevo transactional email API, bulk emails are sent to the users.</li>
            <li><strong>Updates the cache:</strong> Once emails are delivered to the target email addresses, it updates the cache.txt file (inside the project directory) with the new email addresses.</li>
        </ol>
    </section>

    <section>
        <h2>How to use</h2>
        <ol>
            <li><strong>Clone Repo</strong> Clone Repository : Clone this repo using this link - <a href="https://github.com/singharpt/LinkedIn-Automation.git">https://github.com/singharpt/LinkedIn-Automation.git</a></li>
            <li><strong>Create Account at Brevo API</strong> Go to - <a href="https://onboarding.brevo.com/account/register">Brevo API</a></li>
            <li><strong>Select the FREE plan</strong> Select the free tier plan, which provides you with 300 emails a day for free</li>
            <li><strong>Create API Keys</strong> Go to <a href="https://app.brevo.com/settings/keys/api">Click on create "Generate a New API Key". Give it a name and click on generate. MOST IMP: copy the API key to a text file, we will need it later</a></li>
            <li><strong>Update .env file:</strong>
                <ul>
                    <li>Go to the folder you just cloned from the GitHub and open the .env file. Update the key values as per the instructions below:</li>
                    <li><code>API_KEY</code> = Paste the Brevo API key value we just got from the Brevo API Website.</li>
                    <li><code>SENDER_EMAIL</code> = Enter the email address you used to create an account at Brevo. For example, arpit.singh@utdallas.edu</li>
                    <li><code>SENDER_NAME</code> = Enter the name associated with the above email address</li>
                    <li><code>POST_URL</code> = Enter the URL of your post on LinkedIn</li>
                    <li><code>LINKEDIN_EMAIL</code> = Enter your LinkedIn username/email</li>
                    <li><code>LINKEDIN_PASSWORD</code> = Enter your LinkedIn password (Don't worry! The solution works locally on your PC; your data will not be shared with anyone)</li>
                    <li><code>EMAIL_SUBJECT</code> = Enter the subject of the email you want to send (For example, Hi! I got the data you requested in the LinkedIn comment section)</li>
                    <li><code>EMAIL_TEXT</code> = Enter the body of your email.</li>
                    <li><code>EMAIL_HTML</code> = In case you want to add any HTML content, you can; otherwise, you can leave this empty. (DO NOT DELETE THE KEY)</li>
                    <li><code>EMAIL_ATTACHMENT_FOLDER_PATH</code> = This is the path to your folder that contains all the attachments. For example, /Users/Documents/Attachments</li>
                </ul>
            </li>
        </ol>
    </section>

    <section>
        <h2>Tech Stack Used</h2>
        <ul>
            <li>Python</li>
            <li>Object-Oriented Programming</li>
            <li>Selenium</li>
            <li>Brevo SendInBlue Email API</li>
            <li>CronJobs (Linux/MacOS)</li>
        </ul>
    </section>

    <section>
        <h2>Contributions</h2>
        <p>Contributions and improvements to this project are welcome. Please open an issue to discuss any new features, bug fixes, or enhancements you'd like to contribute.</p>
        <p>Please note that this was an experimental project only for learning purposes. I believe a better and optimized solution for the specific problem could be developed.</p>
        <p>If you encounter any issues or have questions, please feel free to contact me directly at <a href="mailto:arpit.singh@utdallas.edu">arpit.singh@utdallas.edu</a>.</p>
    </section>

    <section>
        <h2>Acknowledgments</h2>
        <p>I'd like to thank the open-source community for their contributions and support in developing this tool.</p>
    </section>

</body>

</html>
