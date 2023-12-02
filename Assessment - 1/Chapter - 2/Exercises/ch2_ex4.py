"""
Chapter 2 : Exercise 4 : Registration Page

Writing a program using tkinter module, that creates a GUI as shown in the image

"""

# start of the program

# importing the tkinter module library
from tkinter import *

# creating a variable, for the application window
app = Tk()

# setting the title, dimensions, resizable options for the application window
app.title("Registration Page")
app.geometry("600x700")
app.resizable(0, 0)

# setting the background color
app.configure(background = '#a1b2c4')

################################# CREATING ALL THE REQUIRED WIDGETS/LABELS ETC. ##########################################

# creating a frame to place all the tabs inside the frame
main_frame = LabelFrame(app, width = 525, height = 635, bg = '#1a2b4c', border = 5)

# creating a label as the main heading inside the main frame
main_head = Label(main_frame, font = ('Roboto', 25, 'bold'), text = "Student Managemnet System", fg = '#ffffff', bg = '#1a2b4c')

# creating a sub-heading inside the frame
subhead = Label(main_frame, font = ('Roboto', 20), text = "New Student Registration", fg = '#ffffff', bg = '#1a2b4c')

# creating the student name text label and the text box for the student name 
stdname = Label(main_frame, font = ('Roboto', 14), text = "Student Name", fg = '#ffffff', bg = '#1a2b4c')
stdtext = Text(main_frame, width = 40, height = 2)

# creating the mobile number text label and a text box for it
mobilenum = Label(main_frame, font = ('Roboto', 14), text = "Mobile Number", fg = '#ffffff', bg = '#1a2b4c')
mobilenumtext = Text(main_frame, width = 40, height = 2)


################################## PACKING ALL THE REQURED ITEMS ########################################################

main_frame.pack(pady = 20)                                            # packing the main frame inside the app window
main_head.pack(padx = 10, pady = 10)                                  # packing the main heading inside the mainframe
subhead.pack()                                                        # packing the subheading inside the mainframe
stdname.pack(side = LEFT, padx = 30, pady = 60)                       # packing the student name label text in the mainframe
stdtext.pack(side = RIGHT, padx = 10, pady = 60)                      # packing the textbox for student name   
mobilenum.pack()                     # packing the mobile number label in the mainframe
mobilenumtext.pack()                # packing the text box for the mobile number in the mainframe

# using the mainloop function to run the window, loops the program unlimited number of times, until inturepted by anything
app.mainloop()