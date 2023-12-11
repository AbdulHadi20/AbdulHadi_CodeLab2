"""
Chapter 4 : Exercise 1 : User Information

Develop a GUI App to create a file called bio.txt and write the following information to the file asking user 
to enter the values: Name Age Hometown Each piece of data should be on a new line Once the data has been written 
to the file, read the data from the file and output the data. 

"""

# start of the program

# importing the reqired modules/libraries
from tkinter import *
from tkinter import messagebox
import os

# initializing the root window
window = Tk()

# setting the dimensions. titles, etc
window.title("User Information")
window.geometry("400x350")
window.resizable(0, 0)
window.configure(background = '#363636')

############################ CREATING THE REQUIRED FUNCTIONS ###########################################

# creating a function to save data in a txt file
def save_user_entries():
    user_name = name_entry.get()
    user_age = age_entry.get()
    user_address = homeaddress_entry.get()

    # using try except functions to handle the errors
    # in the try function, we create a file, and save the user entered data in it

    # os.path.join('ch4_ex1', 'bio.txt')
    try: 
        with open("bio.txt", 'w') as file:
            file.write(f'\n Name: {user_name}')
            file.write(f'\n Age: {user_age}')
            file.write(f'\n HomeTown: {user_address}')

        messagebox.showinfo("Success", 'DATA HAS BEEN SAVED SUCCESSFULLY')

    except:
        messagebox.showerror("Error", 'FAILED TO SAVE DATA IN FILE')

# creating a fucntion to read the saved entries from the file
def read_file_data():
    try:
        with open("bio.txt", 'r') as file:
            data = file.read()
        
        messagebox.showinfo("User Information: ", data)

    except:
        messagebox.showerror("Error", 'AN ERROR OCCURED')

############################ CREATING AND DISPLAYING THE REQUIRED WIDGETS ###########################################

# creating a heading label and packing it
heading_label = Label(window, font = ('Arial', 25, 'bold'), text = "User Information", bg = '#363636', fg = '#ffffff')
heading_label.pack(side = TOP, pady = 10)

# creating a frame and packing it
frame = LabelFrame(window, bg = '#363636', border = 0)
frame.pack(pady = 20)

# creating a label and entry for the user to enter their name
name_label = Label(frame, font = ('Inter', 16), text = "Name:", fg = '#ffffff', bg = '#363636')
name_label.grid(row = 0, column = 0, padx = 5, pady = 5)

name_entry = Entry(frame, font = ('Inter', 16), width = 20, border = 0)
name_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

# creating a label and entry for the user to enter their age
age_label = Label(frame, font = ('Inter', 16), text = "Age:", fg = '#ffffff', bg = '#363636')
age_label.grid(row = 1, column = 0, padx = 5, pady = 5)

age_entry = Entry(frame, font = ('Inter', 16), width = 20, border = 0)
age_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

# creating a label and entry for the user to enter their homeaddress
homeaddress_label = Label(frame, font = ('Inter', 16), text = "HomeTown:", fg = '#ffffff', bg = '#363636')
homeaddress_label.grid(row = 2, column = 0, padx = 5, pady = 5)

homeaddress_entry = Entry(frame, font = ('Inter', 16), width = 20, border = 0)
homeaddress_entry.grid(row = 2, column = 1, padx = 5, pady = 5)

# creating two buttons
# creating a button to save data in a txt file
save_data = Button(window, font = ('Arial', 18), text = "Save Data", bg = 'green', padx = 5, pady = 5, command = save_user_entries)
save_data.pack(side = LEFT, anchor = NW, padx = 35, pady = 20)

# creating a button to read data in a txt file
read_data = Button(window, font = ('Arial', 18), text = "Read Data", bg = 'green', padx = 5, pady = 5, command = read_file_data)
read_data.pack(side = RIGHT, anchor = NE, padx = 35, pady = 20)

# running the main window
window.mainloop()

# end of the program