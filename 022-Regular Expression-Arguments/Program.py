#!/usr/bin/python3
# Regular expression-arguments

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""
import re

# Selecting all character including the newline character.
# It means including the whole character.
message = "protect the nation\nand protect the world\n protect the people"
greedy_regex = re.compile(r'.*', re.DOTALL)
match_object = greedy_regex.findall(message)
print(match_object)

# Case insensitive pattern matching.
message = "protect In the nation and protect the world and A Protect the people"
vowel_regex = re.compile(r'[aeiou]', re.IGNORECASE)
# OR
# vowel_regex = re.compile(r'[aeiou]', re.I)
match_object = vowel_regex.findall(message)
print(match_object)

print(" ")
