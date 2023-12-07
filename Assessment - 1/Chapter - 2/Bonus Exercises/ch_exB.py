"""
Chapter 2 : Exercise B : Age Calculator


Writing a program in GUI tkinter that asks the user for their date of birth, and then tells them their age
Hint: Can use the date from datetime package
"""

# start of the program

# importing the required libraries and modules
from tkinter import *
from datetime import date

# initializing the root window
root = Tk()

# setting the dimensions, title, background etc. of the page
root.title("Age Calculator")
root.geometry("400x400")
root.resizable(0, 0)
root.configure(background = 'skyblue')

################################ CREATING THE FUNCTION FOR THE BUTTON TO CALCULATE #################################################

# creating a function to calculate the age

def age_cal():
    dob = dob_entry.get()
    # mob = mob_entry.get()
    # yob = yob_entry.get()

    # check if user entry is a digit
    if dob.isdigit():
        user_dob = dob
        # user_mob = int(mob)
        # user_yob = int(yob)

        date_today = date.today()

        dob_date = date.fromisoformat(user_dob)

        age = date_today - dob_date 

        # age = date_today - birthdate.year - ((date_today.month, birthdate.day) < (birthdate.month, birthdate.day))

        result_str.set(f"\n You are {age} years old")

    else: 
        result_str.set("\n ERROR !! Please enter only digits")




################################ CREATING ALL THE REQUIRED WIDGETS #################################################

# creating a heading label
heading = Label(root, font = ('Arial', 18, 'bold'), text = "AGE CALCULATOR", bg = 'skyblue', fg = 'blue')

# creating a frame so that the labels and entry widgets are neatly displayed
mainframe = LabelFrame(root, bg = 'skyblue', border = 0)

# label that displays a message to tell the user to enter their day
user_dob = Label(mainframe, font = ('Arial', 12), text = "Please enter your Day of Birth = ", bg = 'skyblue', fg = 'blue')

# label that displays a message to tell the user to enter their month
# user_mob = Label(mainframe, font = ('Arial', 12), text = "Please enter your Month of Birth = ", bg = 'skyblue', fg = 'blue')

# label that displays a message to tell the user to enter their year
# user_yob = Label(mainframe, font = ('Arial', 12), text = "Please enter your Year of Birth = ", bg = 'skyblue', fg = 'blue')

# an entry widget for the user to tell their date of birth
dob_entry = Entry(mainframe, font = ('Arial', 12), width = 15)

# an entry widget for the user to tell their date of birth
# mob_entry = Entry(mainframe, font = ('Arial', 12), width = 15)

# an entry widget for the user to tell their date of birth
# yob_entry = Entry(mainframe, font = ('Arial', 12), width = 15)

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
# user_mob.grid(row = 1, column = 0, padx = 5, pady = 20)                      # displays the label widget for the user to read
# mob_entry.grid(row = 1, column = 1, padx = 5, pady = 20)                     # displays the entry widget for the user to type the dob
# user_yob.grid(row = 2, column = 0, padx = 5, pady = 20)                      # displays the label widget for the user to read
# yob_entry.grid(row = 2, column = 1, padx = 5, pady = 20)                     # displays the entry widget for the user to type the dob
calculatebtn.pack(side = TOP, anchor = N, padx = 5, pady = 5)                # displays the button that will perform the calculation
result.pack(side = BOTTOM, anchor = S, padx = 5, pady = 3)                   # displays the result

# running the root window (mainloop)
root.mainloop()

# end of program