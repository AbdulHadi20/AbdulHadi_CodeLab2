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

# setting the window, to be fixed, forbidding resizing (will be decided)
apptab.resizable(1, 1)

# setting the background color for the window
apptab.configure(background = '#ffe5b4')

# creating a frame to place all the text-boxes, buttons, etc. in one place
mainframe = LabelFrame(apptab, bg = '#1a2b45', border = 10)

# creating a label inside a frame..
loginheading = Label(mainframe, text = "LOGIN", fg = '#ffffff', bg = '#1a2b45', font = ('Helavatica', 30, 'bold'))

# creating a label for username and password
user_label = Label(mainframe, text = 'Username: ', fg = '#ffffff', bg = '#1a2b45', font = ('Helavatica', 15, 'bold'))
pass_label = Label(mainframe, text = 'Password: ', fg = '#ffffff', bg = '#1a2b45', font = ('Helavatica', 15, 'bold'))

# creating text boxes for username and password
user_text = Text(mainframe, width = 30, height = 1)
pass_text = Text(mainframe, width = 30, height = 1)

# using grid() to display the frame
mainframe.grid(padx = 100, pady = 100, row = 10, column = 10 )

# displaying the heading inside the frame
loginheading.grid(padx = 50, pady = 50, row = 5, column = 8)

# creating a button to confirm login details
login_btn = Button(mainframe, text = 'Log In', width = 15, height = 2, bg = '#ffe5b4', fg = '#1a2b45')

# displaying the username and password labels inside the frame
user_label.grid()
pass_label.grid()

# displaying the text boxes for username and password
user_text.grid()
pass_text.grid()

# displaying the button insiade the mainframe
login_btn.grid()

# using mainloop to display/run the main apptab window
apptab.mainloop()
