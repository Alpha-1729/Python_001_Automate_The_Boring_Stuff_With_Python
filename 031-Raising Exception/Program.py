#!/usr/bin/python3
# Raising exception

"""
>>>> Python raises exception when try to run invalid code.
>>>> The error message we get in the shell is called a 'Traceback'.
>>>>
>>>>
>>>>
"""
import traceback

# Raising an exception
# raise Exception('This is the error message')

# Saving the Traceback in a log file
try:
    raise Exception('This is the error message')
except:
    error_file = open('error_log.txt', 'a')
    error_file.write(traceback.format_exc())
    error_file.close()
    print('Error message has been added to the log file.')

print(" ")
