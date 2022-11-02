#!/usr/bin/python3
# Dictionary

"""
>>>>Dictionary doesn't have any order.
        {"pk" : 12, "ls" : 21} == {"ls" : 21, "pk" : 12} # Both are same.
>>>>
>>>>
>>>>
>>>>
"""

import pprint

# Dictionary methods
animal_dic = {"lion": 32, "elephant": 100, "ant": 1}
print(animal_dic.keys())
print(animal_dic.values())
print(animal_dic.items())

# Printing the key and values in the dictionary
for key, value in animal_dic.items():
    print(key, value)

# get() method in dictionary
# print(animal_dic["giraffe"]) -> It will throw an error, because key is not in the dictionary.
# If key is not in the dictionary second argument will be returned.
print(animal_dic.get("giraffe", "Not Found"))

# setdefault method
# Used to add a key and value if key doesn't exist.
# If key already exist, it doesn't update the value.
animal_dic = {"lion": 32, "elephant": 100, "ant": 1}

if "tiger" not in animal_dic:
    animal_dic["tiger"] = 90
# OR
animal_dic.setdefault("tiger", "90")

# For counting the each letters in long string
message = "hello how are you doing i am learning the python programming language"
data = {}
for letter in message.upper():
    data.setdefault(letter, 0)
    data[letter] = data[letter] + 1

# Print the content in the dictionary in a nice format.
pprint.pprint(data)

# Store the formatted data in string format.
text_format_data = pprint.pformat(data)
print(text_format_data)
print(" ")