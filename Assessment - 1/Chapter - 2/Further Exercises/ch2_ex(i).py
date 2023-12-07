"""
Chapter 2 : Exercise I : Count Characters

Writing a program that asks the user to enter a string, then counts out the vowels and consonants, and special characters

"""

# start of the program

# importing the tkinter module
from tkinter import *

# creating the root window
root =Tk()

# setting the dimensions, title, etc
root.title("Count Characters")
root.geometry("600x400")
root.resizable(0, 0)
root.configure(background = 'grey')

###################### CREATING REQUIRED FUNCTIONS ###################################################

###################### CREATING REQUIRED WIDGETS ####################################################

# creating a heading label
heading_label = Label(root, font = ('Arial', 20, 'bold'), text = "Count Characters", bg = 'grey')

# creating a frame for the label and entry widgets
frame = LabelFrame(root, border = 0, bg = 'grey') 

# creating a label for the user's instruction
label = Label(frame, font = ('Arial', 14), text = "Please type in a sentence = ", bg = 'grey')

# creating an entry widget for the user's typing
textbox = Text(frame, font = ('Arial', 14), width = 20, height = 3)

# creating a button to start counting the characters
button = Button(root, font = ('Arial', 16, 'bold'), text = "Count Characters", bg = 'brown', fg = 'white', padx = 5, pady = 5 )

###################### DISPLAYING THE REQURIED WIDGETS ##############################################

heading_label.pack(side = TOP, anchor = N, padx = 3, pady = 7)
frame.pack(side = TOP, anchor = N, padx = 3, pady = 7)
label.grid(row = 0, column = 0, padx = 5, pady = 5)
textbox.grid(row = 0, column = 1, padx = 5, pady = 5)
button.pack(side = TOP, anchor = N, padx = 3, pady = 7)


# running the root window (mainloop)
root.mainloop()