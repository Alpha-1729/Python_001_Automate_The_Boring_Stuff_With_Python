#!/usr/bin/python3
# Regular expression findall

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""
import re

# findall without groups in the content.
message = "My phone number is 444-555-8965 and call me evening in 256-854-7455"
phone_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d')

# match_object will be a list of strings.
match_object = phone_regex.findall(message)
print(match_object)

# findall with groups in the content.
message = "My phone number is 444-555-8965 and call me evening in 256-854-7455"
phone_regex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d))')

# Contains tuple in the list based on the group in the regular expression pattern.
match_object = phone_regex.findall(message)
print(match_object)

print(" ")