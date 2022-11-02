#!/usr/bin/python3
# Regular expression-searching at the start and end of the string

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""
import re

# Search at the beginning
message = "Hello World!"
start_regex = re.compile(r'^Hello')
match_object = start_regex.findall(message)
print(match_object)

# Search at the end
# Using the dollar symbol.
message = "Hello World!"
end_regex = re.compile(r'World!$')
match_object = end_regex.findall(message)
print(match_object)

# Searching the exact match string using the ^ and &
# Finding pattern that look like '1213com'
message = "154545com"
# The string must startswith a number and end with "com", and should not have any character in between.
both_regex = re.compile(r'^\d+com$')
match_object = both_regex.findall(message)
print(match_object)

print(" ")
