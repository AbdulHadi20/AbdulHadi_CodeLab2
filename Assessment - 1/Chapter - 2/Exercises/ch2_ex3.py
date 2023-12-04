"""
Chapter 2 : Exercise 3 : Login Page

Writing a pyhton program using tkinter library to create a login page.

"""

# start of the program  (clearing out once the button is pressed, u make that)

# calling the tkinter library
from tkinter import *

# initializing the root window
apptab = Tk()

#setting the default dimensions for the app, setting the title
apptab.title("Login Page")
apptab.geometry("800x500")

# setting the window, to be fixed, forbidding resizing
apptab.resizable(0, 0)

# setting the background color for the window
apptab.configure(background = '#ffe5b4')

# creating a function to clear out the user entered values once the button is pressed
def btnpress(user_text, pass_text):
    user_text = user_text.get()
    pass_text = pass_text.get()


# creating a frame to place all the text-boxes, buttons, etc. in one place
mainframe = LabelFrame(apptab, bg = '#1a2b45', border = 10)

# creating a label inside a frame..
loginheading = Label(mainframe, text = "LOGIN", fg = '#ffffff', bg = '#1a2b45', font = ('Helavatica', 50, 'bold'))

# creating a label for username and password
user_label = Label(mainframe, text = 'Username: ', fg = '#ffffff', bg = '#1a2b45', font = ('Helavatica', 15, 'bold'))
pass_label = Label(mainframe, text = 'Password: ', fg = '#ffffff', bg = '#1a2b45', font = ('Helavatica', 15, 'bold'))

# creating text boxes for username and password
user_text = Text(mainframe, width = 50, height = 1, pady = 2)
pass_text = Text(mainframe, width = 50, height = 1, pady = 2)

# using grid() to display the frame
mainframe.grid(row = 0, column = 3, padx = 30, pady = 15)

# displaying the heading inside the frame
loginheading.grid(padx = 150, pady = 75, column = 1)

# creating a button to confirm login details
login_btn = Button(mainframe, text = 'Log In', width = 15, height = 2, bg = '#ffe5b4', fg = '#1a2b45', font = ('Helavatica', 15, 'bold')
                   , command = btnpress)

# displaying the username and password labels inside the frame
user_label.grid(row = 1, column = 0, pady = 2, padx = 40)
pass_label.grid(row = 2, column = 0, pady = 2, padx = 40)

# displaying the text boxes for username and password
user_text.grid(row = 1, column = 1, pady = 2)
pass_text.grid(row = 2, column = 1, pady = 2)

# displaying the button insiade the mainframe
login_btn.grid(row = 3, column = 1, pady = 20)

# using mainloop to display/run the main apptab window
apptab.mainloop()

# end of the program