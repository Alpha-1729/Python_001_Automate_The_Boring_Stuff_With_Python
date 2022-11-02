#!/usr/bin/python3
# Regular expression part 5

"""
>>>> Greedy matching.
        Match the longest string possible.
>>>> Non-Greedy matching.
        Match the shortest string possible.
>>>>
>>>>
"""
import re

# Greedy match: Find the max len pattern.
message = "my number is 123456789"
digit_regex = re.compile(r'(\d){3,5}')
match_object = digit_regex.search(message)
print(match_object.group())

# Non greedy match: Find the min len pattern.
message = "my number is 123456789"
digit_regex = re.compile(r'(\d){3,5}?')
match_object = digit_regex.search(message)
print(match_object.group())

print(" ")
