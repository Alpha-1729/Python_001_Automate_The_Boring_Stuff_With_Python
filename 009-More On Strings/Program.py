#!/usr/bin/python3
# More on strings

"""
>>>>
>>>>
>>>>
>>>>
>>>>
"""
# Raw string
print(r'hello this is mary\'s car.')

# String methods
text = "hello world"
print(text.title())  # Return string as a title Eg: Hello World

text = "hello world"
print(text.islower())  # Return True

text = "HELLO WORLD"
print(text.isupper())  # Return True

text = ""
print(text.isupper())  # Return False
print(text.islower())  # Return False

# Other methods
"""
isalpha() -> letters only.
isalnum() -> letters and numbers only.
isdecimal() -> numbers only.
isspace() -> whitespace only.
istitle() -> title case only
"""
# join method
names = ["cat", "dog", "bat"]
print(", ".join(names))  # return 'cat, dog, bat'

# rjust, ljust, center method
text = "hello"
text.rjust(10)  # -> "     hello"
text.rjust(10, "=")  # -> "=====hello"

text.ljust(10)  # -> "hello     "
text.ljust(10, "=")  # -> "hello====="

text.center(10)  # -> "   hello  "
text.ljust(10, "=")  # -> "===hello==="

# strip(), rstrip(), lstrip() methods
text = "   hello   "
text.strip()  # -> "hello"
text.lstrip()  # -> "hello   "
text.rstrip()  # -> "   hello"

text = "SpamSpamBaconSpamEggsSpamSpam"
# -> "BaconSpamEggs"  Remove these characters from both ends.
text.strip("ampS")

print(" ")