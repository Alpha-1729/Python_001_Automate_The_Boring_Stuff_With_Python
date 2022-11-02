#!/usr/bin/python3
# Selenium module

"""
>>>> Download geckodriver from this link
        Link :https://github.com/mozilla/geckodriver/releases
        Extract to C:\Program Files
        Add this path to path variables.
>>>> Selenium documentation
        link: https://selenium-python.readthedocs.io/
>>>> pip install selenium
>>>> Currently I am using selenium with the firefox.
>>>> A lot of methods in the older version of selenium is not currently available in the latest version.
        I updated the code based on the latest version of the selenium.
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
import time

gecko_driver_path = r'C:\Program Files\geckodriver-v0.32.0-win64\geckodriver.exe'

firefox_service = Service(gecko_driver_path)

browser = webdriver.Firefox(service=firefox_service)

# Open the browser and go to the url.
browser.get("https://automatetheboringstuff.com")

element = browser.find_element(
    "xpath", "/html/body/div/main/div/ul[2]/li[1]/a")
element.click()

# Wait for 2 seconds.
time.sleep(2)

# Exiting a browser instance.
browser.quit()

firefox_service = Service(gecko_driver_path)
# Again opening the browser.
browser = webdriver.Firefox(service=firefox_service)

# Go to gmail
browser.get("https://www.gmail.com")

# Getting the xpath of the email field.
email_element = browser.find_element(
    "xpath", '''//*[@id="identifierId"]''')

# Add a email and click on the submit.
email_element.send_keys("python@gmail.com")
time.sleep(2)
email_element.send_keys(Keys.RETURN)

time.sleep(2)
browser.back()          # Back button
time.sleep(2)
browser.forward()       # Forward button
time.sleep(2)
browser.refresh()       # Refresh the page
time.sleep(2)
browser.quit()          # Quit the browser.

# Reading the content in the webpage
firefox_service = Service(gecko_driver_path)

# Again opening the browser.
browser = webdriver.Firefox(service=firefox_service)

browser.get('https://automatetheboringstuff.com/')

paragraph_element = browser.find_element(
    "xpath", '''/html/body/div/main/div/p[4]''')

paragraph = paragraph_element.text
print(paragraph)

full_html_content = browser.find_element("xpath", "html")
print(full_html_content.text)

print(" ")
