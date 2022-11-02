#! python3
# Shebang line for windows
# Introduction

"""
>>>> Official website -> https://automatetheboringstuff.com/
>>>> Running a python script
        python hello.py 
        OR
        py hello.py
        OR 
        pyw hello.py -> windowless running
>>>> Use pastebin or gist.gisthub.com for sharing code in the stack overflow.
>>>> 42.0 and 42 are equal in python.
>>>> http://pythontutor.com/ is a website to visualize the python code.
>>>> Blank string '' is a falsey value and a valid string is a truthy value.
>>>> 0, 0.0 and empty string are falsey values in python.
>>>> __init__, __name__, __package__, __spec__ are called the dunder variables.
     __init__ -> read as dunder init
     __name__ -> read as dunder name ...
"""

# Expressions
# Expressions evaluates to a single value.
# Expressions = Values + Operators
# Eg: 2 + 2

# Statement.
# The code that doesn't evaluate to a single expression.
# They are also known as instructions.

# String multiplication.
student_name = 'Alice '
print(student_name * 3)

# Verifying the user input string.
my_name = input()
if my_name:
    print("you entered a valid name")
else:
    print("You doesn't enter anything")

# Line continuation (\)
random_paragraph = "my name is sam" + \
    "peter bellingham" + \
    "i agree with you"
print(random_paragraph)
