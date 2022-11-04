#!/usr/bin/python3
# Regular expression part 2

"""
>>>> If the regular expression can't find any pattern, it will return None.
>>>> | character to get one of many possible group.
>>>>
>>>>
>>>>
"""
import re

# If you want to find a pattern that contain a parenthesis, Use escape character.
message = "call me in (454) 556-5456 or in (544) 654-8789"
phone_num_regex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
match_object = phone_num_regex.findall(message)
print(match_object)

# Using | character to get one of many possible group.
# I want to get all words like Batman, Batmobile, Batbat, Batcar
message = "Batmobile is good for charging and nothing"
bat_regex = re.compile(r'Bat(man|bat|mobile|car)')
match_object = bat_regex.search(message)
print(match_object.group())   # -> print matching text
print(match_object.group(1))  # -> print matching text in the group

print(" ")
