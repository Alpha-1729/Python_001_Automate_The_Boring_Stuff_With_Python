#!/usr/bin/python3
# Logging module

"""
>>>> Logging is a great way to understand what happening in the program.
>>>> Logging vs print()
        If we use print in the program, we have to uncomment all print statement after use.
        Logging can be disabled with a single line statement in the top of the program.
>>>> Log levels.
        logging.DEBUG        -> (lowest)
        logging.INFO
        logging.WARNING
        logging.ERROR
        logging.CRITICAL    -> (highest)
>>>>
>>>>
"""
import logging

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Logging to a file
# If we avoid the "filename" parameter, It will print all the log.
logging.basicConfig(filename='log.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Disable all logging message
# logging.disable(logging.CRITICAL)  # Disabling all levels below the Critical

logging.debug('Starting of the program')

def factorial(n):
    logging.debug('Starting of the factorial (%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total = total*i
        logging.debug('i is (%s), total is (%s)' % (i, total))
    logging.debug('Return value is (%s)' % (total))
    return total

print(factorial(5))
logging.debug('End of the program')
