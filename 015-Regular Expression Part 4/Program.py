#!/usr/bin/python3
# Regular expression part 4

"""
>>>> + -> 1 or more time.
>>>> * -> O or more time.
>>>> {} -> find pattern with exact number of times.
"""
import re

# + means 1 or more time.
# Use \+ for an actual + symbol.
message = "I am a Batman"
bat_regex = re.compile(r'Bat(wo)+man')
match_object = bat_regex.findall(message)
print(match_object)

message = "I am a Batwoman"
match_object = bat_regex.search(message)
print(match_object.group())

message = "I am a Batwowowowoman"
match_object = bat_regex.search(message)
print(match_object.group())

# * means 0 or more time.
# use \* for an actual * symbol.
message = "I am a Batman"
bat_regex = re.compile(r'Bat(wo)*man')
match_object = bat_regex.search(message)
print(match_object.group())

message = "I am a Batwoman"
match_object = bat_regex.search(message)
print(match_object.group())

message = "I am a Batwowowowoman"
match_object = bat_regex.search(message)
print(match_object.group())

# {} -> exact number of times.
# Finding a pattern 'Ha' 3 times exactly like 'HaHaHa'
message = "my message is HaHaHa"
ha_regex = re.compile(r'(Ha){3}')
match_object = ha_regex.search(message)
print(match_object.group())

# {min, max} -> a range of numbers
# {, 5} between 0-5
# {3, } greater than 3
# Finding a pattern 'Ha' 2-4 times
message = "my message is HaHaHaHaHaHaHaHa"
ha_regex = re.compile(r'(Ha){2,4}')
match_object = ha_regex.search(message)
print(match_object.group())

print(" ")
