"""
Chapter 2 : Exercise 3 : Login Page

Writing a pyhton program using tkinter library to create a login page.

"""

# start of the program 

# calling the tkinter library
from tkinter import *

# initializing the root window
apptab = Tk()

#setting the default dimensions for the app, setting the title
apptab.title("Login Page")
apptab.geometry("600x400")

# setting the window, to be fixed, forbidding resizing
apptab.resizable(0, 0)

# creating a frame to place all the text-boxes, buttons, etc. in one place
mainframe = LabelFrame(apptab, bg = '#1a2b45', border = 20)

# creating a label inside a frame..
loginheading = Label(mainframe, text = "Log In / Sign Up")

# using grid() to display the frame
mainframe.grid(padx = 100, pady = 100)
loginheading.grid(padx = 50, pady = 50, row = 1, column = 8)

# using mainloop to display/run the main apptab window
apptab.mainloop()
