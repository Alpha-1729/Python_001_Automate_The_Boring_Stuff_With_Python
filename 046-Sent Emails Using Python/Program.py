#!/usr/bin/python3
# Sent emails using python

"""
>>>>SMTP
        The protocol that sending emails uses is SMTP.
        Simple Mail Transfer protocol.
>>>> Add an app-password
        Link: https://devanswers.co/create-application-specific-password-gmail/
        And create a app password
>>>> Check for google app specific password.
>>>>
>>>>
"""
import smtplib
import os

from_email = os.environ.get("MY_EMAIL", -1)
password = os.environ.get("MY_EMAIL_PASSWORD", -1)
to_email = from_email

# Creating a connection object.
con = smtplib.SMTP("smtp.gmail.com", 587)

# We also get the temporary IPv6 Address.
print(con.ehlo())  # Creating a connection

# Creating a tls encryption, so that our password is safe.
con.starttls()

# log in
con.login(from_email, password)

# Sending the email
# This will return a dictionary of email address it fail to sent.
# If the dictionary is empty, that means, all mail has been sent.
# You can also sent multiple email using the sendemail method, see the documentation.
con.sendmail(from_email, to_email,
             'Subject: So long seeing you.\n\nDear sir,\nYour mail has been cracked.')

# Quitting the connection.
con.quit()

print(" ")
