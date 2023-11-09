"""
Description: autoclicker to get very fast score and reach 100th percentile.
Author: Lars Anderson
Date: 231107
Usage: on human benchmark website.
"""
# IMPORTS
import time
import threading
from pynput.mouse import Button, Controller
from PIL import ImageGrab

# VARIABLES
button = Button.left
pixel_not_found = True
green_found = 0
green = (75, 219, 106)

# CLASSES
class ClickMouse(threading.Thread):
    def __init__(self, button):
        super(ClickMouse, self).__init__()
        
    def run(self):
        mouse.press(self.button)
        mouse.release(self.button)

# MAIN PROGRAM

mouse = Controller()
click = ClickMouse(button)

while green_found < 5:
    img = ImageGrab.grab(bbox=None)
    pixel = img.getpixel((764, 407))
    if pixel == green:
        click.run()
        time.sleep(2)
        click.run()
        green_found += 1

# 764, 407 middle of laptop screen
# 2911, 504 middle of 2nd monitor