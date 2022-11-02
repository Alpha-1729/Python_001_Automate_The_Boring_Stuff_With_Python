#!/usr/bin/python3
# Pyautogui taking screenshot

"""
>>>> For screenshot to work on linux.
        sudo apt-get install scrot
>>>> Chapter 17 in the automatetheboringstuff book covers about the pillow library.

>>>> Game(Sushi Go Round) using the pyautogui.
        Link: https://github.com/asweigart/sushigoroundbot
>>>>
>>>>
"""
import pyautogui

pyautogui.screenshot('screenshot.jpg')

# For image recognition on the screen.
# Create a cropped image of the object to be recognized using ShareX or LightShot application.
# Return a tuple of 4 integers.
coordinate = pyautogui.locateOnScreen('cropped_image.png')
print(coordinate)
pyautogui.moveTo(coordinate[0], coordinate[1], duration=2)

# Locating the center of the detected object
# Return a tuple of two integers.
center = pyautogui.locateCenterOnScreen("cropped_image.png")
print(center)

# Clicking on the that point.
pyautogui.click(center)  # Center is a tuple value.
pyautogui.click(center[0], center[1])  # These are integer values.

print(" ")
