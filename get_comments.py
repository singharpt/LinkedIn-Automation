from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from dotenv.main import load_dotenv
import os
load_dotenv()

# get the enviroment variables
linkedIn_email = os.environ['LINKEDIN_EMAIL']
linkedIn_password = os.environ['LINKEDIN_PASSWORD']
post_url = os.environ['POST_URL']


def get_emails_from_comments():
    """
    This function returns the email ids present in the comment section of the target linkedIn post
    Output: List of dictionary
    """

    # Create a Chrome WebDriver instance using the automatically managed ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # options=options
    driver = webdriver.Chrome()

    # Navigate to the post url
    driver.get(post_url)

    # go to sign in
    sign_in_btn = driver.find_element(By.CLASS_NAME, 'main__sign-in-link')
    sign_in_btn.click()

    # Find the search input element and type a search query
    email = driver.find_element(By.ID, 'username')
    email.send_keys(linkedIn_email)
    password = driver.find_element(By.ID, 'password')
    password.send_keys(linkedIn_password)
    password.submit()

    # Find the comments box using the appropriate selector
    comment_elements = driver.find_elements(
        By.CLASS_NAME, 'comments-comment-item')

    # list to store all emails mentioned in the comments
    email_list = []

    # Iterate through each comment element and extract the email addresses
    for comment_element in comment_elements:

        # Extract the HTML content of the comment
        comment_html = comment_element.get_attribute('outerHTML')

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(comment_html, 'html.parser')

        # Find the span element with dir="ltr"
        ltr_span = soup.find('span', attrs={'dir': 'ltr'})

        # Extract and get the text inside the span if found
        if ltr_span:
            email_inside_span = ltr_span.get_text()
            email_list.append({"Email": email_inside_span})

    # Close the WebDriver when you're done
    driver.quit()

    return email_list
