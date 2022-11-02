#!/usr/bin/python3
# Checking email inbox using imap

"""
>>>> IMAP
        Internet Message Access Protocol.
>>>> pip install imapclient
     pip install pyzmail36
>>>> Error pyzmail:
        link: https://stackoverflow.com/questions/40924672/pip-install-pyzmail-error-message
>>>> Installing pyzmail
        easy_install pyzmail -> if pip install fails.
>>>> Imap Documentation
        link: https://imapclient.readthedocs.org
>>>> pyzmail Documentation.
        link: http://www.magiksys.net/pyzmail/
>>>> Imap search keys are available in the Table 18.3 in the AutomateTheBoringStuff.pdf in the 000-Resources folder.

"""
import imapclient
import pyzmail
import os

from_email = os.environ.get("MY_EMAIL", -1)
password = os.environ.get("MY_EMAIL_PASSWORD", -1)

conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)
conn.login(from_email, password)

# Set readonly=True, if you dont want to delete the email.
conn.select_folder('INBOX', readonly=True)

# Finding the emails
# For getting all emails.
all_uids = conn.search(['ALL'])

# Searching some email ids
uids = conn.search('SINCE 20-Aug-2019')

# Printing the unique-ids(uids)
# print(uids)

# Getting the email -> 16195 in uids
raw_message = conn.fetch([16195], ['BODY[]', 'FLAGS'])
# print(raw_message)

# Formatting the raw message using the pyzmail
message = pyzmail.PyzMessage.factory(raw_message[16195][b'BODY[]'])

# Get subjects
print(message.get_subject())

# Get from address
print(message.get_address('from'))

# Get to addresses
print(message.get_address('to'))

# Get bcc addresses
print(message.get_address('bcc'))

# Checking the text part and html part
print(message.html_part)
print(message.text_part)

# Getting the text part of the mail
inner_message = message.text_part.get_payload().decode('UTF-8')
print(inner_message)

# Checking the encoding used in the email
print(message.text_part.charset)

# Listing all folders in the gmail
# Each item in the list is the tuple.
# Third value in the tuple is the actual folder in the gmail.
print(conn.list_folders())

# Deleting the emails.
conn.select_folder('INBOX', readonly=False)
uids = conn.search('ON 14-Jul-2020')
print(uids)

# I want to delete email with unique-id -> 20998 and 20999
# Pass list of uids for delete
conn.delete_messages([20998, 20999])

# Logout
conn.logout()

print(" ")
