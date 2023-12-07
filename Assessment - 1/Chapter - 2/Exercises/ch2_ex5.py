"""
Chapter 2 : Exercise 5 : Calculator

Writing a program that creates a GUI calculator, that performs basic arithmetic operations
- Addition
- Subtraction
- Multiplication
- Division
- Modulus

We can ask the user to enter values, and select operations to perform

"""

# start of the program 

# importing the tkinter module library
from tkinter import *

# initializing the root window, along with title, geometry, and resizable options
appwindow = Tk()                                # the variable that has the root window initialized
appwindow.geometry("500x500")                   # the geomtery o the application window
appwindow.title("MY CALCULATOR")                # the title displayed on the title bar of the window
appwindow.resizable(0, 0)                       # does not allow the user to resize the applicatin window 
appwindow.configure(background = 'green')       # setting the background color of the app window


############################ CREATING FUNCTIONS FOR ARITHMETIC OPERATIONS #############################################

# creating a funtion that takes values from the user and gets the sum
def addition():
    value_1 = num1_userentry.get()
    value_2 = num2_userentry.get()

    # now we have to check if the values entered are digigts or not
    if value_1.isdigit() and value_2.isdigit():
        # if they are digitts, then since the values would be in str format, we convert them into float values
        userentry_1 = float(value_1)
        userentry_2 =  float(value_2)

        ans = userentry_1 + userentry_2

        finalans.set(f"\n The sum of {value_1} and {value_2} is {ans}")

    else: 
        finalans.set("\n ERROR, PLEASE ENTER DIGITS ONLY")

# creating a funtion that takes values from the user and gets the difference
def subtraction():
    value_1 = num1_userentry.get()
    value_2 = num2_userentry.get()

    # now we have to check if the values entered are digigts or not
    if value_1.isdigit() and value_2.isdigit():
        # if they are digitts, then since the values would be in str format, we convert them into float values
        userentry_1 = float(value_1)
        userentry_2 =  float(value_2)

        ans = userentry_1 - userentry_2

        finalans.set(f"\n The difference of {value_1} and {value_2} is {ans}")

    else: 
        finalans.set("\n ERROR, PLEASE ENTER DIGITS ONLY")

# creating a funtion that takes values from the user and gets the product
def multiplication():
    value_1 = num1_userentry.get()
    value_2 = num2_userentry.get()

    # now we have to check if the values entered are digigts or not
    if value_1.isdigit() and value_2.isdigit():
        # if they are digitts, then since the values would be in str format, we convert them into float values
        userentry_1 = float(value_1)
        userentry_2 =  float(value_2)

        ans = userentry_1 * userentry_2

        finalans.set(f"\n The product of {value_1} and {value_2} is {ans}")

    else: 
        finalans.set("\n ERROR, PLEASE ENTER DIGITS ONLY")

# creating a funtion that takes values from the user and gets the division
def division():
    value_1 = num1_userentry.get()
    value_2 = num2_userentry.get()

    # now we have to check if the values entered are digigts or not 
    if value_1.isdigit() and value_2.isdigit():
        # if they are digitts, then since the values would be in str format, we convert them into float values
        userentry_1 = float(value_1)
        userentry_2 =  float(value_2)

        ans = userentry_1 / userentry_2

        finalans.set(f"\n The divison of {value_1} and {value_2} is {ans}")

    else: 
        finalans.set("\n ERROR, PLEASE ENTER DIGITS ONLY")

# creating a funtion that takes values from the user and gets the remainder
def modulus():
    value_1 = num1_userentry.get()
    value_2 = num2_userentry.get()

    # now we have to check if the values entered are digigts or not
    if value_1.isdigit() and value_2.isdigit():
        # if they are digitts, then since the values would be in str format, we convert them into float values
        userentry_1 = float(value_1)
        userentry_2 =  float(value_2)

        ans = userentry_1 % userentry_2

        finalans.set(f"\n The remainder of {value_1} and {value_2} is {ans}")

    else: 
        finalans.set("\n ERROR, PLEASE ENTER DIGITS ONLY")

# creating a fucnction to clear out the entry fields
def clear_values():
    num1_userentry.delete(0, "end")
    num2_userentry.delete(0, "end")


########################### SETTING UP THE TKINTER WINDOW / STYLING LABELS & WIDGETS #################################    

# creating a heading
head_label = Label(appwindow, text = "Welcome to the calculator !", font = ('Helavatica', 25, 'bold'), bg = 'green', fg = 'skyblue')

# creating a frame to set the labels and entry widgets nicely
user_entry_frame = LabelFrame(appwindow, bg = 'green', border = 0)

# setting the labels and entry widgets for the values to be entered by the user
num1_label = Label(user_entry_frame, font = ('Roboto', 16, 'bold'),text = "Please Enter the first value = ", fg = 'white', bg = 'green')
num1_userentry = Entry(user_entry_frame, width = 10, font = ('Roboto', 16))

num2_label = Label(user_entry_frame, font = ('Roboto', 16, 'bold'),text = "Please Enter the second value = ", fg = 'white', bg = 'green')
num2_userentry = Entry(user_entry_frame, width = 10, font = ('Roboto', 16))


# creating a frame to set all the buttons neatly presented
btns_frame = LabelFrame(appwindow, bg = 'green', border = 0)

# creating the buttons for each operation
addbtn = Button(btns_frame, font = ('Roboto', 16), text = 'Addition +', fg = 'white', bg = 'red', border = 2, command = addition)
subbtn = Button(btns_frame, font = ('Roboto', 16), text = 'Subtraction -', fg = 'white', bg = 'red', border = 2, command = subtraction)
mulbtn = Button(btns_frame, font = ('Roboto', 16), text = 'Multiplication x', fg = 'white', bg = 'red', border = 2, command = multiplication)
divbtn = Button(btns_frame, font = ('Roboto', 16), text = 'Division /', fg = 'white', bg = 'red', border = 2, command = division)
modbtn = Button(btns_frame, font = ('Roboto', 16), text = 'Modulus %', fg = 'white', bg = 'red', border = 2, command = modulus)
clear = Button(btns_frame, font = ('Roboto', 16), text = 'Clear', fg = 'white', bg = 'black', border = 2, command = clear_values)

# creating a label for the results
finalans = StringVar()
finalanslabel = Label(appwindow, font = ('Helavatica', 16, 'bold'), fg = 'white', bg = 'green', textvariable = finalans)


######################### DISPLAYING THE LABELS AND WIDGETS INSIDE THE APP WINDOW ###################################

head_label.pack(anchor = N, padx = 30, pady = 10)                       # packing the heading in the main root window
user_entry_frame.pack()                                                 # packing the frame for user entry
num1_label.grid(row = 0, column = 0, pady = 10, padx = 5)               # using grid to specify the coordinates of the num1 label
num1_userentry.grid(row = 0, column = 1, pady = 10, padx = 5)           # using grid to display the num1 entry widget
num2_label.grid(row = 1, column = 0, pady = 10, padx = 5)               # using grid to display label for num2
num2_userentry.grid(row = 1, column = 1, pady = 10, padx = 5)           # using grid to display the entry widget for num2
btns_frame.pack(anchor = W, padx = 5)                                   # packing the frame for all the btns
addbtn.grid(row = 0, column = 0, padx = 5, pady = 10)                   # using grid to display the addition button
subbtn.grid(row = 0, column = 1, padx = 5, pady = 10)                   # using grid to display the subtraction button
mulbtn.grid(row = 1, column = 0, padx = 5, pady = 10)                   # using grid to display the multiplication button
divbtn.grid(row = 1, column = 1, padx = 5, pady = 10)                   # using grid to display the division button
modbtn.grid(row = 2, column = 0, padx = 5, pady = 10)                   # using grid to display the modulus button
clear.grid(row = 2, column = 1, padx = 5, pady = 10)                    # using grid to display the clear button
finalanslabel.pack(side = BOTTOM, anchor = S, padx = 5, pady = 20)      # using grid to display the final answer of the calculations


# running the root window
appwindow.mainloop()

# end of program