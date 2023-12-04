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

# start of the program (NEED TO MAKE SURE THAT THE CALCULATIONS ARE WORKING)

# importing the tkinter module library
from tkinter import *

# initializing the root window, along with title, geometry, and resizable options
appwindow = Tk()                                # the variable that has the root window initialized
appwindow.geometry("500x500")                   # the geomtery o the application window
appwindow.title("MY CALCULATOR")                # the title displayed on the title bar of the window
appwindow.resizable(0, 0)                       # does not allow the user to resize the applicatin window 
appwindow.configure(background = 'green')       # setting the background color of the app window


############################ CREATING FUNCTIONS FOR ARITHMETIC OPERATIONS #############################################

# creating a funtion that takes values from the user
def user_values(selectionofuser):
    value_1 = num1_userentry.get()
    value_2 = num2_userentry.get()

    # now we have to check if the values entered are digigts or not
    if value_1.isdigit() and value_2.isdigit():
        # if they are digitts, then since the values would be in str format, we convert them into float values
        userentry_1 = float(value_1)
        userentry_2 =  float(value_2)

        # now, we perform the arithemetic opertations

        if selectionofuser == addbtn:
            finalans.set(userentry_1 + userentry_2)
        
        elif selectionofuser == subbtn:
            finalans.set(userentry_1 - userentry_2)

        elif selectionofuser == mulbtn:
            finalans.set(userentry_1 * userentry_2)

        elif selectionofuser == divbtn:
            finalans.set(userentry_1 / userentry_2)

        elif selectionofuser == modbtn: 
            finalans.set(userentry_1 % userentry_2)

    
    else:
        finalans.set("ERROR - PLEASE ENTER NUMBERS ONLY")

    
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
addbtn = Button(btns_frame, font = ('Roboto', 16), text = 'Addition +', fg = 'white', bg = 'red', border = 2, command = user_values)
subbtn = Button(btns_frame, font = ('Roboto', 16), text = 'Subtraction -', fg = 'white', bg = 'red', border = 2, command = user_values)
mulbtn = Button(btns_frame, font = ('Roboto', 16), text = 'Multiplication x', fg = 'white', bg = 'red', border = 2, command = user_values)
divbtn = Button(btns_frame, font = ('Roboto', 16), text = 'Division /', fg = 'white', bg = 'red', border = 2, command = user_values)
modbtn = Button(btns_frame, font = ('Roboto', 16), text = 'Modulus %', fg = 'white', bg = 'red', border = 2, command = user_values)


# creating a label for the results
finalans = StringVar()
finalanslabel = Label(btns_frame, font = ('Helavatica', 20, 'bold'), fg = 'white', bg = 'green', textvariable = finalans)


######################### DISPLAYING THE LABELS AND WIDGETS INSIDE THE APP WINDOW ###################################

head_label.pack(anchor = N, padx = 30, pady = 10)                       # packing the heading in the main root window
user_entry_frame.pack()                                                 # packing the frame for user entry
num1_label.grid(row = 0, column = 0, pady = 10, padx = 5)               # using grid to specify the coordinates of the num1 label
num1_userentry.grid(row = 0, column = 1, pady = 10, padx = 5)           # using grid to display the num1 entry widget
num2_label.grid(row = 1, column = 0, pady = 10, padx = 5)               # using grid to display label for num2
num2_userentry.grid(row = 1, column = 1, pady = 10, padx = 5)           # using grid to display the entry widget for num2
btns_frame.pack(anchor = W, padx = 5)                                   # packing the frame for all the btns
subbtn.grid(row = 1, column = 0, padx = 5, pady = 10)                   # using grid to display the addition button
mulbtn.grid(row = 2, column = 0, padx = 5, pady = 10)                   # using grid to display the subtraction button
divbtn.grid(row = 3, column = 0, padx = 5, pady = 10)                   # using grid to display the multiplication button
addbtn.grid(row = 0, column = 0, padx = 5, pady = 10)                   # using grid to display the division button
modbtn.grid(row = 4, column = 0, padx = 5, pady = 10)                   # using grid to display the modulus button
finalanslabel.grid(row = 3, column = 1)                                 # using grid to display the final answer of the calculations


# running the root window
appwindow.mainloop()

# end of program