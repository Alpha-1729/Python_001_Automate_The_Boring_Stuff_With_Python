#!/usr/bin/python3
# Regular expression part3

"""
>>>> ? in regular expression means 0 or 1 time.
>>>>
>>>>
>>>>
>>>>
"""
import re

# ? -> group appear 0 times or 1 time.
message = "This is Batman."
bat_regex = re.compile(r'Bat(wo)?man')
match_object = bat_regex.search(message)
print(match_object.group())

message = "This is Batwoman."
match_object = bat_regex.search(message)
print(match_object.group())

# Checking for phone numbers with or without std code.
message = "call me in  568-5455 or evening in 444-555-1456"
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
match_object = phone_regex.search(message)
print(match_object.group())

# Literally looking for a ? mark
message = "Do you have dinner?"
dinner_regex = re.compile(r'dinner\?')
match_object = dinner_regex.search(message)
print(match_object.group())
