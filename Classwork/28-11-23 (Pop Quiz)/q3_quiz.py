"""
Writing a program that creates a simple GUI application, and has the following:

- Button
- Displays a message when the button is pressed
- performs an action

"""

# start of the program

# importing the tkinter module
from tkinter import *

# initializing the root window
appwindow = Tk()

# setting the title of the window
appwindow.title('GUI Test')

# setting the dimensions of the window
appwindow.geometry("400x400")

# setting the resizable option to false
appwindow.resizable(0, 0)

# creating a function for the button, when the button is pressed
def press():
    print('\n You have pressed a button.')

# creating a button with red background, white text, with a width of  10 and height of 2, and the function is triggered once the button is pressed
btn = Button(appwindow, bg = 'red', width = 10, height = 2, fg = 'white', text = 'I am a button', command = press)

# creating a random text box with a width and height
textbox = Text(appwindow, width = 15, height = 3)

# packing the text box to display the box on the top of the screen
textbox.pack(side = TOP)

# packing the button to display on the top of the screen, but will be displayed just below the textbox
btn.pack(side = TOP)

# using the mainloop function to run the root window
appwindow.mainloop()
