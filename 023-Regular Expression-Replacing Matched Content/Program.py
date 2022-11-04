#!/usr/bin/python3
# Regular expression-replacing matched content

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""
import re

# Replacing the matched content.
message = "Agent Alice give secret document to the Agent Johny."
name_regex = re.compile(r'Agent \w+')
match_object = name_regex.findall(message)
print(match_object)

# Replacing the content with the sub() method
print(name_regex.sub("UNKNOWN_NAME", message))

# Getting the first letter of the name
message = "Agent Alice give secret document to the Agent Johny."
name_regex = re.compile(r'Agent (\w)\w*')
match_object = name_regex.findall(message)
print(match_object)

# Replacing the content with the sub() method
# \1 represent the group 1 in the pattern match.
print(name_regex.sub(r'Agent \1***', message))

print(" ")
