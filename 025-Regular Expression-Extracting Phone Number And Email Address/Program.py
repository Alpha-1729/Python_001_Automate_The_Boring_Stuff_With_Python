#!/usr/bin/python3
# Regular expression-extracting phone number and email address

"""
>>>> In this we are going to grab phone number and email address from a file containing a huge list of phone numbers and email address.

>>>>
>>>>
>>>>
>>>>
"""
import re
import pyperclip

# Phone number patterns
phone_regex = re.compile(r'''
# 415-562-5548, 555-4848, (415) 895-4566, 555-0000 (ext 12345 OR ext. 12345 OR x12345)
(
((\d\d\d)|(\(\d\d\d\)))?            # Area code (optional)
(\s|-)                              # First separator -> space or hyphen
\d\d\d                              # First 3 digit
-                                   # Separator
\d\d\d\d                            # Last 4 digits
(((ext(\.)?\s)|x)                   # Extension word-part (optional)
(\d{2,5}))?                         # Extension number part (optional) 
)
''', re.VERBOSE)

# Email pattern.
email_regex = re.compile(r'''
# some.+_thing@something.com
[a-zA-Z0-9._+]+         # Name part
@                       # @ symbol
[a-zA-Z0-9._+]+         # domain name part
''', re.VERBOSE)

# Getting the text in the clipboard
text = pyperclip.paste()

# Extract the email and phone numbers.
extracted_phone = phone_regex.findall(text)
extracted_email = email_regex.findall(text)

all_phone_number = [phoneNumbers[0] for phoneNumbers in extracted_phone]

# Copy extracted email and phone numbers to clipboard
final_data = '\n'.join(all_phone_number) + '\n' + '\n'.join(extracted_email)
print(final_data)

# Store the email and phone on the clipboard.
pyperclip.copy(final_data)
print(" ")
