#!/usr/bin/python3
# Gui automation-control mouse

"""
>>>> pip install pyautogui
>>>> PyAutoGUI Documentation:
        link: https://pyautogui.readthedocs.org
>>>> Coordinate of the screen:
        0, 0 -> left top
        x, y ->width, height 

>>>> For stopping the mouse automation.
        Manually move the mouse cursor to (0,0)
        It will create and exception and stop the program.
>>>> For getting the mouse position realtime
        Open cmd
        Open python shell
        Import pyautogui
        Type pyautogui.displayMousePosition() in python shell.
        It also show the RGB value of the color in the screen pixel where mouse is located.
"""
import pyautogui

# Getting the screen size.
print(pyautogui.size())
width, height = pyautogui.size()
print(width, height)

# Getting the current mouse position.
print(pyautogui.position())

# Moving the mouse pointer.
pyautogui.moveTo(500, 500)
pyautogui.moveTo(700, 600, duration=2.5)  # With duration.

# Moving the cursor with respect to the current position.
pyautogui.moveRel(-300, -300)
pyautogui.moveRel(200, 400, duration=2.5)  # With duration.

# Clicking using the mouse.
pyautogui.click(554, 666)

# Middle click
pyautogui.middleClick(55, 156)

# Right click
pyautogui.rightClick(46, 545)

# Double click
pyautogui.doubleClick(145, 545)

# Click and drag mouse from current position to that coordinate.
pyautogui.dragTo(55, 41, duration=1.5)

# Click and drag mouse with respect to the current position.
pyautogui.dragRel(55, 41, duration=1.5)

print(" ")
