#!/usr/bin/python3
# Files and folders

"""
>>>>File path separator
        \       -> Windows
        /       -> Linux & Mac
>>>>Current and previous directory
        .       -> Current directory
        ..      -> Previous directory
>>>>
>>>>
>>>> 
"""
import os

# Will print the path separator in the current operating system.
print(os.sep)

# Create a file path from folders.
print(os.path.join("Folder1", "Folder2", "Folder3", "Folder4"))

# Converting relative path to absolute path.
# Print the absolute file path of the file.txt assuming it is in current directory.
print(os.path.abspath("file.txt"))

# Check whether the argument passed is a absolute path or not.
print(os.path.isabs("file.txt"))  # return True or False.

# Find the relative path.
# Return Pen\Cap\Pencil.png
print(os.path.relpath(r'C:\Users\Pen\Cap\Pencil.png', r'C:\Users'))

# Dirname and Basename
file_path = r'C:\windows\system32\calc.exe'
print(os.path.basename(file_path))  # Return file name or folder name.
print(os.path.dirname(file_path))    # Return the folder path.

# Checking existence of a file
print(os.path.exists(file_path))  # Return True or False.

# Check for file or folders.
print(os.path.isfile(file_path))  # Check whether the argument is a file.
print(os.path.isdir(file_path))  # Check whether the argument is a folder.

# Getting the size of a file (in bytes).
print(os.path.getsize(file_path))  # Works only on file

# Print the size of the folder only (4096 bytes), not size of folder content.
print(os.path.getsize('C:\\'))

print(' ')
