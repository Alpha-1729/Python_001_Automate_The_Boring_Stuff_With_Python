#!/usr/bin/python3
# Request module

"""
>>>> For downloading files from the web.
>>>> pip install requests
>>>> About unicode in python.
        Both have same content.
        LINK: http://bit.ly/unipain
        OR
        LINK: https://nedbatchelder.com/text/unipain.html
>>>> About requests module.
        LINK: https://requests.readthedocs.io/en/master/
>>>>
"""
import requests

# Url of the romeo and juliet story.
url = "http://automatetheboringstuff.com/files/rj.txt"

response = requests.get(url)  # Getting the response.

print(response.status_code)

# Status code is 200, If successful.
# Else 404, Like file not found.
# Or any other status code.

# Getting the first 500 character in the text file.
print(response.text[:500])

# raise_for_status() method will raise an exception if the download fails.
print(response.raise_for_status())

# Saving the text in wb mode
play_file = open('RomeoAndJuliet.txt', 'wb')
for chunk in response.iter_content(10000):   # reading 10000 bytes each time.
    play_file.write(chunk)
play_file.close()

print(" ")
