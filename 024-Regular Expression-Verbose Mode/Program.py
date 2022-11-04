#!/usr/bin/python3
# Regular expression-verbose mode

"""
>>>> Verbose mode allow use to add pattern in multiline comment.
    We can also add comment in the pattern in multiline comment.
>>>>
>>>>
>>>>
>>>>
"""
import re

# Using the verbose mode.
message = "my phone number is 715-515-5155 call me on 545-515-5154"
number_regex = re.compile(r'''
\d\d\d  # Area code
-
\d\d\d
-
\d\d\d\d''', re.VERBOSE)
match_object = number_regex.findall(message)
print(match_object)

# Using the verbose mode and ignorecase and dotall
message = "my phone number is 715-515-5155 call me on 545-515-5154"
number_regex = re.compile(r'''
\d\d\d  # area code
-
\d\d\d
-
\d\d\d\d''', re.VERBOSE | re.IGNORECASE | re.DOTALL)  # Bitwise or operator in python.
match_object = number_regex.findall(message)
print(match_object)

print(" ")
