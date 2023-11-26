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
appwindow.geometry("500x400")
appwindow.resizable(1, 1)

# creating the two frames 
frame1 = LabelFrame(appwindow, border = 5, padx = 5, pady = 5)
frame2 = LabelFrame(appwindow, border = 5, padx = 5, pady = 5)

#packing the frames to display on the main window
frame1.pack(side = LEFT, expand = 1, fill = BOTH)
frame2.pack(side = RIGHT, expand = 1, fill = BOTH)

# creating labels inside the frame as reuired
label1 = Label(frame1, text = "A", bg = '#012A4A', fg = 'white', width = 10, height = 10)
label2 = Label(frame1, text = "B", width = 10, height = 10)
label3 = Label(frame2, text = "C", width = 10, height = 10)
label4 = Label(frame2, text = "D", bg = '#012A4A', fg = 'white', width = 10, height = 10)

# packing the labels to be displayed inside the frame
label1.pack(side = TOP, fill = BOTH, expand = 1)
label2.pack(side = BOTTOM, fill = BOTH, expand = 1)
label3.pack(side = TOP, fill = BOTH, expand = 1)
label4.pack(side = BOTTOM, fill = BOTH, expand = 1)

# running the root widow
appwindow.mainloop()

# end of the program