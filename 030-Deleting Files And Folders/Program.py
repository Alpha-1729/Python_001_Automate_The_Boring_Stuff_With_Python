#!/usr/bin/python3
# Deleting files and folders

"""
>>>> pip install send2trash
        For moving deleted files into the recycle bin.
>>>> Dry Run (Terminology)
        Comment out the line of code to delete the file.
        First print all the files that you want to delete.
        Then Uncomment the line of code to delete the file.
>>>>
>>>>
>>>>
"""
import os
import shutil
import send2trash

# Deleting  a file
os.unlink('file.txt')  # Delete a single file.

# Removing a directory.
os.rmdir("anyFolder")  # For removing only empty directory.

# Removing non-empty directory
shutil.rmtree('anyFolder')

# Removing a file and move to recycle bin.
send2trash.send2trash('file.txt')

print(" ")
