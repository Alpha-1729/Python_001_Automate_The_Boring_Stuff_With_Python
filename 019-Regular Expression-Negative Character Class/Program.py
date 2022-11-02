#!/usr/bin/python3
# Regular expression-negative character class

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""
import re

# ^ means negation in the character class only.
# Finding consecutive consonants.
message = "this is my dog and you cannot find it anywhere"
consonant_regex = re.compile(r'[^aeiouAEIOU]{2}')
match_object = consonant_regex.findall(message)
print(match_object)

print(" ")
