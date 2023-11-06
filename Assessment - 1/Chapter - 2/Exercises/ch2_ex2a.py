"""
Chapter 2 : Exercise 2 : Managing Layouts : 2a, Using Packs

Writing a program that has 4 label widgets using pack() geometry as shown in the image. The first image shows the original display
and the second one after it gets resized.
"""

# start of the program

# calling the tkinter module
from tkinter import *

# initializing the root window, representing it with a variable
app = Tk()

# creating a title for the window
app.title("Managing Layouts: Using Packs")

# creating the labels
lbl1 = Label(app, bg = 'red', text = 'A', width = 12, bd = 5, relief = GROOVE)
lbl2 = Label(app, bg='yellow', text = 'B', width = 12)
lbl3 = Label(app, bg = 'blue', text = 'C', width = 12)
lbl4 = Label(app, bg = 'white', text = 'D', width = 12)

# packing (displaying) the labels in the window, and placing them at their positions as shown
lbl1.pack(side = 'top', fill = X, expand = 1)
lbl2.pack(side = 'bottom')
lbl3.pack(side = 'left', expand = 1)
lbl4.pack(side = 'right')

# now, running the root window 
app.mainloop()

# end of the program