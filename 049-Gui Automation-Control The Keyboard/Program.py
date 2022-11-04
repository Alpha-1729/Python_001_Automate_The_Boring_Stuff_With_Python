#!/usr/bin/python3
# Gui automation-control the keyboard

"""
>>>> If you want to run two statement in the shell, separate the two commands by "semicolon(;)".
>>>>
>>>>
>>>>
>>>>
"""
import pyautogui

# Clicking and typing, better try it in the shell.
pyautogui.click(200, 200)
pyautogui.typeWrite("Hello World")

# Adding delay in typing each word.
pyautogui.typeWrite("I am python", interval=0.2)

# Pressing the left arrow key twice.
pyautogui.typeWrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)

# Getting all the keyboard keys.
print(pyautogui.KEYBOARD_KEYS)

# Pressing the single key.
pyautogui.press('f1')

# Pressing combination of keys.
pyautogui.hotkey('shift', '2')

print(" ")
