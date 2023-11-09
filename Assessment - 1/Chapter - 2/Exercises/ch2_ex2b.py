"""
Chapter 2 : Exercise 2 : Managing Layouts : 2b, Square Grid

Writing a program to create a GUI by using pack(). Doing the following tasks in it:

- With the pack layout manager, creating the labels inside the frame. A and B inside the left frame. C and D inside the right frame. 
- Using pack() to align A and C on the top, and B and D at the bottom. 
- Supporting resizing. Also using the expand and fill property to make sure the labels grow when the window is stretched.
- Keeping the borders of the frames to 5px. 
"""

# start of the program

# calling the tkinter module
from tkinter import *

# initializing the root window
appwindow = Tk()

# giving a title to the window
appwindow.title("Square Grids")

# setting the window size and making it resizable
appwindow.geometry("600x600")
appwindow.resizable(1, 1)

frame1 = Frame(appwindow, )
