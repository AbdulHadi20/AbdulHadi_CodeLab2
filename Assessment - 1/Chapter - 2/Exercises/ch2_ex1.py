"""
Chapter 2 : Exercise 1 : Welcome

Writing a program to develop a GUI to do the following using the tkinder module

- create a label to display the welcome message and change the label font style (font name, bold, size)
- set the default window size
- disable resizing the window
- add background color to the window

"""

# start of the program 

# calling the tkinter module
from tkinter import *

# now, we initialize the root window, also we will save the initialization in a variable
root_window = Tk()

# setting the default window size, and disabling the resizing for the window, because I can
root_window.geometry("600x600") #sizing
root_window.resizable(0, 0) #hehe, now it cannot be resized...

# creating a label and displaying it on the gui window 
welcome = Label(root_window, text="MY FIRST GUI WINDOW", font=("Helvetica", 20, "bold")) # creating label
welcome.pack() # displaying label

# adding a background color
root_window.configure(background="#a1b2c3") # im not sure about the name of the color, just wrote a random hex code for fun (light purple imo)

#running the root window
root_window.mainloop()

# end of the program 