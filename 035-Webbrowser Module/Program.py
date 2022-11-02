#!/usr/bin/python3
# Webbrowser module

"""
>>>> webbrowser module is used to open a url in browser.
>>>> Here we are going to make webbrowser to open a location in google maps.
        Location is taken from the command line argument.
        OR
        Location is taken from the clipboard.
>>>> Sample google maps url
        https://www.google.com/maps/place/London,+UK/@51.5283063,-0.3824708,10z/data=!3m1!4b1!4m5!3m4!1s0x47d8a00baf21de75:0x52963a5addd52a99!8m2!3d51.5073509!4d-0.1277583
>>>> Webbrowser module will open the url using the operating systems default browser.
>>>>
"""
import webbrowser
import pyperclip
import sys

if len(sys.argv) > 1:
    # Getting the location from the command line.
    address = ' '.join(sys.argv[1:])
else:
    # Copying the location from the clipboard.
    address = pyperclip.paste()

full_url = 'https://www.google.com/maps/place/' + address

# Opening the location in the google maps.
webbrowser.open(full_url)
