#!/usr/bin/python3
# Regular expression character class

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""
import re

# Shorthand character class.
"""
\d  -> Any numeric digit from 0-9.
\D  -> Any character that is not a numeric digit from 0-9.
\w  -> Any letter, numeric digit, or the underscore character. (Group of "word" characters.)
\W  -> Any character that is not a letter,numeric digit, or the underscore character.
\s  -> Any space , tab, or newline character. (Group of "space" characters.)
\S  -> Any character that is not a space, tab, or newline. 
"""

# Find pattern with number followed by a word.
message = "12 drummers drumming, 11 pipers piping, 10 lords a leaping"
word_regex = re.compile(r'\d+\s\w+')
match_object = word_regex.findall(message)
print(match_object)

# Making custom character class
message = "anImalisgOodforyoU"
vowel_regex = re.compile(r'[aeiouAEIOU]')
match_object = vowel_regex.findall(message)
print(match_object)

# Making custom character class
# Adding range of characters.
message = "animaL123isgoodforyou"
vowel_regex = re.compile(r'[a-zA-Z]')
match_object = vowel_regex.findall(message)
print(match_object)

# Find two consecutive vowels.
message = "animalisgoodforyouII"
vowel_regex = re.compile(r'[aeiouAEIOU]{2}')
match_object = vowel_regex.findall(message)
print(match_object)

print(" ")
