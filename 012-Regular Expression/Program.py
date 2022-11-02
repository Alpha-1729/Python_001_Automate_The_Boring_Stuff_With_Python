#!/usr/bin/python3
# Regular expression

"""
>>>> \d represent a number in regular expression.
>>>>
>>>>
>>>>
>>>>
"""
import re

message = "Call me in 454-556-5456 or in 544-654-8789"

# Creating a regular expression object.
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# Searching the first phone number.
# Prints the first occurrence of the pattern.
match_object = phone_num_regex.search(message)
print(match_object.group())

# Searching all phone number in the message.
match_object = phone_num_regex.findall(message)
print(match_object)

# Getting the area code in the phone number
phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
match_object = phone_num_regex.search(message)
print(match_object.group())   # -> printing the full number
print(match_object.group(0))  # -> printing the full number
print(match_object.group(1))  # -> printing the std code
print(match_object.group(2))  # -> printing the actual number.

print(" ")
