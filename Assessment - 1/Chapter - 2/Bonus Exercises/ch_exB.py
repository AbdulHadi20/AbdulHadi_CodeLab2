"""
Chapter 2 : Exercise B : Age Calculator


Writing a program in GUI tkinter that asks the user for their date of birth, and then tells them their age
Hint: Can use the date from datetime package
"""

# start of the program

# importing the required libraries and modules
from tkinter import *
from datetime import datetime

# initializing the root window
root = Tk()

# setting the dimensions, title, background etc. of the page
root.title("Age Calculator")
root.geometry("600x400")
root.resizable(0, 0)
root.configure(background = 'skyblue')

################################ CREATING THE FUNCTION FOR THE BUTTON TO CALCULATE #################################################

# creating a function to calculate the age

def age_cal():                             
    date_today = datetime.today()                              # getting tdoay's date and storing it in a var
    dob = dob_entry.get()                                      # getting the user's date of birth and storing it
    user_birthday = datetime.strptime(dob, "%d/%m/%Y")         # converting the user's dob into a datetime format

    # calculating the years of age of the user
    user_year = date_today.year - user_birthday.year 

    # calculating the months and days as well
    if (date_today.month, date_today.day) == (user_birthday.month, user_birthday.day): # runs if user's month and day is same as today's
        result_str.set(f"Happy Birthday Human! Have a nice one.. \n You are now {user_year} years old")

    elif (date_today.month, date_today.day) < (user_birthday.month, user_birthday.day): # runs user's birthday hasn't come this year
        user_current = user_year - 1
        
        result_str.set(f"Congratulations, You are {user_current} years old. ")

    else:  # runs if user enters invalid date (needs fin)
        result_str.set(f"Congratulations, You are {user_year} years old")

################################ CREATING ALL THE REQUIRED WIDGETS #################################################

# creating a heading label
heading = Label(root, font = ('Arial', 18, 'bold'), text = "AGE CALCULATOR", bg = 'skyblue', fg = 'blue')

# creating a frame so that the labels and entry widgets are neatly displayed
mainframe = LabelFrame(root, bg = 'skyblue', border = 0)

# label that displays a message to tell the user to enter their day
user_dob = Label(mainframe, font = ('Arial', 12), text = "Please enter your Day of Birth (d-m-y)= ", bg = 'skyblue', fg = 'blue')

# an entry widget for the user to tell their date of birth
dob_entry = Entry(mainframe, font = ('Arial', 12), width = 15, text = "dd-mm-yyyy")

# creating a  button to calculate the age of the user
calculatebtn = Button(root, font = ('Arial', 14), text = "Calculate Age !", bg = 'blue', fg = 'skyblue', padx = 5, pady = 5, command = age_cal)

# creating a label to display the result
result_str = StringVar()
result = Label(root, font= ('Arial', 14), textvariable = result_str, bg = 'skyblue', fg = 'blue')


################################ DISPLAYING ALL THE REQUIRED WIDGETS #################################################

heading.pack(side = TOP, anchor = N, padx = 5, pady = 15)                    # displays the main heading
mainframe.pack(side = TOP, pady = 20)                                        # displays the mainframe below the heading
user_dob.grid(row = 0, column = 0, padx = 5, pady = 20)                      # displays the label widget for the user to read
dob_entry.grid(row = 0, column = 1, padx = 5, pady = 20)                     # displays the entry widget for the user to type the dob 
calculatebtn.pack(side = TOP, anchor = N, padx = 5, pady = 5)                # displays the button that will perform the calculation
result.pack(side = BOTTOM, anchor = S, padx = 5, pady = 3)                   # displays the result

# running the root window (mainloop)
root.mainloop()

# end of program