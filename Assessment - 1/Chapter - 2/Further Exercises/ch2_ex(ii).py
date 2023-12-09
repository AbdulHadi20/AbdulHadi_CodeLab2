"""
Chapter 2 : Exercise II : Capitalize Letters

Create a GUI program in tkinter that takes the input, and changes all the letters to uppercase

"""

# start of the program

# importing the required modules/libraries
from tkinter import *

# initializing the root window
window = Tk()

# setting the title, dimensions, resizing, etc.
window.title("CAPITALIZE LETTERS")             # sets the title
window.geometry("800x500")                     # sets the dimensions
window.resizable(0, 0)                         # sets the resizing option false
window.configure(background = 'red')           # sets the background color

############################## CREATING THE REQUIRED FUNCTION ####################################

# creating a function to capitalize all the letters
def scream():
    user_sentence = msgtext_str.get()             # saving the entry in a variable

    upper_user_sentence = user_sentence.upper()

    result_str.set(f"{upper_user_sentence}")    # printing the result with the upper()

# creating a function to delete everything in the textbox
def clear():
    msgtext.delete(0, "end")


############################## CREATING THE REQUIRED WIDGETS ####################################

# creating a heading label
headlabel = Label(window, font = ('Arial', 18, 'bold'), text = "WELCOME TO SCREAMISTAN !!", bg = 'red', fg = 'white')

# creating a frame for the msg label and entry widget
framemain = LabelFrame(window, bg = 'red', border = 0)

# creating a label to display the message
msglabel = Label(framemain, font = ('Arial', 14, 'bold'), text = "LET IT OUT !! --> ", bg = 'red', fg = 'white')

# creating a textbox
msgtext_str = StringVar()
msgtext = Entry(framemain, width = 25, textvariable = msgtext_str, font = ('Arial', 14) )

# creating the button to capitalize all the letters
btn = Button(framemain, font = ('Arial', 16, 'bold'), text = "SCREAM...!!", bg = 'white', fg = 'red', padx = 5, pady = 5, command = scream)

# creating a clear button
btn_clear = Button(framemain, font = ('Arial', 16, 'bold'), text = "Clear", bg = 'white', fg = 'red', padx = 5, pady = 5, command = clear)

# creating a label to display the result
result_str = StringVar()
result = Label(window, font = ('Arial', 14), textvariable = result_str, bg = 'red', fg = 'white')

############################## DISPLAYING THE REQUIRED WIDGETS ####################################

headlabel.pack(side = TOP, anchor = N, padx = 3, pady = 7)           # sets the heading in the window
framemain.pack(side = TOP, anchor = N, padx = 5, pady = 8)           # sets the frame in the window
msglabel.grid(row = 0, column = 0, padx = 5, pady = 5)               # sets the label message in the window 
msgtext.grid(row = 0, column = 1, padx = 5, pady = 5)                # sets the entry in the window 
btn_clear.grid(row = 1, column = 1, padx = 5, pady = 15)             # sets the button in the window
btn.grid(row = 1, column = 0, padx = 5, pady = 15)                   # sets the clear button in the window
result.pack(side = BOTTOM, anchor = S, padx = 5, pady = 20)          # sets the result to display

# running the main window (mainloop)
window.mainloop()

# end of the program