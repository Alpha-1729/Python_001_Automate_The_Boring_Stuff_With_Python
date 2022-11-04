#!/usr/bin/python3
# Regular expression-wildcard character

"""
>>>> "." -> anything except newline character
>>>>
>>>>
>>>>
>>>>
"""
import re

# Finding a pattern like hat cat bat
# It look for a single character.
message = "my hat is like you heat your bat and that is sat on pat"
at_regex = re.compile(r'.at')
match_object = at_regex.findall(message)
print(match_object)

# Finding a pattern like that hat cat bat
# Finding all words that has "at" after it.  including " hat" "that" " bat"
message = "my hat is like you heat your bat and that is sat on pat"
at_regex = re.compile(r'.{1,2}at')
match_object = at_regex.findall(message)
print(match_object)

# .*  -> to match anything -> it is a greedy search
message = "First Name: Dony Last Name: Peter "
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
match_object = name_regex.findall(message)
print(match_object)

# .*?  -> to match anything -> it is a non greedy search
message = "<to serve human > for dinner>"
non_greedy_regex = re.compile(r'<(.*?)>')
match_object = non_greedy_regex.findall(message)
print(match_object)

# Greedy search
greedy_regex = re.compile(r'<(.*)>')
match_object = greedy_regex.findall(message)
print(match_object)

print(" ")
