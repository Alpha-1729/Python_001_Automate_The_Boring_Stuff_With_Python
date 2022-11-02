#!/usr/bin/python3
# Copy module

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""
import copy
num_list_one = [1, 2, 3]

# Then num_list_one and num_list_two are at exactly different location in the memory.
num_list_two = copy.deepcopy(num_list_one)

print(" ")
