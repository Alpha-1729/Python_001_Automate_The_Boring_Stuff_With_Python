#!/usr/bin/python3
# Shelve module

"""
>>>>Binary shelf file (with the help of the shelve module)
        For storing variables like list, dictionary and other complex data structure in a file.
>>>>
>>>>
>>>>
>>>>
"""
import shelve

shelf_file = shelve.open('mydata')
shelf_file['animal'] = ['dog', 'cat', 'lion', 'monkey']
shelf_file['car'] = ['venture', 'odie', 'fiat', 'bens']
shelf_file.close()

# Grab the data like a dictionary
shelf_file = shelve.open('mydata')
print(shelf_file['animal'])

# Getting the key and values in the file object.
print(list(shelf_file.keys()))          # Printing the keys.
print(list(shelf_file.values()))        # printing the values.
shelf_file.close()
