"""
Chapter 2 : Exercise 4 : Registration Page

Writing a program using tkinter module, that creates a GUI as shown in the image

"""

# start of the program

# importing the tkinter module library
from tkinter import *
import os
# importing the PIL library (photo imaging library), as python does not support images with png format
from PIL import ImageTk, Image

# creating a variable, for the application window
app = Tk()

# setting the title, dimensions, resizable options for the application window
app.title("Registration Page")
app.geometry("600x700")
app.resizable(0, 1)

# setting the background color
app.configure(background = '#a1b2c4')

################################# CREATING ALL THE REQUIRED WIDGETS/LABELS ETC. ##########################################

# creating a frame to place all the tabs inside the frame
main_frame = LabelFrame(app, width = 525, height = 635, bg = '#1a2b4c', border = 5)

# creating a label as the main heading inside the main frame
main_head = Label(main_frame, font = ('Roboto', 25, 'bold'), text = "Student Managemnet System", fg = '#ffffff', bg = '#1a2b4c')

# creating a sub-heading inside the frame
subhead = Label(main_frame, font = ('Roboto', 20), text = "New Student Registration", fg = '#ffffff', bg = '#1a2b4c')

# adding the image inside a canvas with the university logo at the top
# canvas = Canvas(app, width = 50, height = 5)    
# bathspalogobanner = ImageTk.PhotoImage(Image.open("bsu_logo_image.png"))
# canvas.create_image(0, 0, side = TOP, image = bathspalogobanner)

script_directory = os.path.dirname(os.path.realpath(__file__))
img = Image.open(os.path.join(script_directory, "BSULOGO.png"))
logobsubanner = ImageTk.PhotoImage(img)
imglabel = Label(app, image = logobsubanner)

# creating the student name text label and the text box for the student name 
stdname = Label(main_frame, font = ('Roboto', 14), text = "Student Name", fg = '#ffffff', bg = '#1a2b4c')
stdtext = Text(main_frame, width = 40, height = 2)

# creating the mobile number text label and a text box for it
mobilenum = Label(main_frame, font = ('Roboto', 14), text = "Mobile Number", fg = '#ffffff', bg = '#1a2b4c')
mobilenumtext = Text(main_frame, width = 40, height = 2)

# creating the label and text box for email id
email_id = Label(main_frame, font = ('Roboto', 14), text = "Email ID", fg = '#ffffff', bg = '#1a2b4c')
email_idbox = Text(main_frame, width = 40, height = 2)

# creating the label and text box for home address
homeaddress = Label(main_frame, font = ('Roboto', 14), text = "Home Address", fg = '#ffffff', bg = '#1a2b4c')
homeaddressbox = Text(main_frame, width = 40, height = 2)

# creating the label and text box for the gender
gender = Label(main_frame, font = ('Roboto', 14), text = "Gender", fg = '#ffffff', bg = '#1a2b4c')

# genderdisplay = StringVar()
# genderdrop = OptionMenu(main_frame, genderdisplay, "Male", "Female", "Confused")
genderdrop = Text(main_frame, width = 40, height = 2)

# creating a label and radio buttons for courses enrolled
coursesenrolled = Label(main_frame, font =('Roboto', 14), text = "Course Enrolled", fg = '#ffffff', bg = '#1a2b4c')

# radio buttons
course_rd1 = Radiobutton(main_frame, text = "BSc CC", bg = '#1a2b4c', fg = '#ffffff')    # radio button 1 
course_rd2 = Radiobutton(main_frame, text = "BSc CY", bg = '#1a2b4c', fg = '#ffffff')    # radio button 2
course_rd3 = Radiobutton(main_frame, text = "BSc PSY", bg = '#1a2b4c', fg = '#ffffff' )   # radio button 3
course_rd4 = Radiobutton(main_frame, text = "BA & BM", bg = '#1a2b4c', fg = '#ffffff')   # radio button 4

# creating a label and checkboxes for the languages known option
languages = Label(main_frame, font = ('Roboto', 14), text = "Languages known", fg = '#ffffff', bg = '#1a2b4c')

# checkboxes
checkbox1 = Checkbutton(main_frame, text = 'English', bg = '#1a2b4c', fg = '#ffffff')
checkbox2 = Checkbutton(main_frame, text = 'Tagalog', bg = '#1a2b4c', fg = '#ffffff')
checkbox3 = Checkbutton(main_frame, text = 'Hindi/Urdu', bg = '#1a2b4c', fg = '#ffffff')

# creating the text message and its progress meter
rates = Label(main_frame, font = ('Roboto', 15, 'bold'), text = "Rate your English communication skills", fg = '#ffffff', bg = '#1a2b4c')
progressmeter = Scale(main_frame, from_ = 0, to = 100, orient = HORIZONTAL, width = 40, troughcolor = '#ffffff')




################################## PACKING ALL THE REQURED ITEMS ########################################################

imglabel.pack(side = TOP)                                 # packing the header image in the window
main_frame.pack(pady = 20)                                            # packing the main frame inside the app window
main_head.pack(padx = 10, pady = 10)                                  # packing the main heading inside the mainframe
subhead.pack()                                                        # packing the subheading inside the mainframe
stdname.pack()                       # packing the student name label text in the mainframe
stdtext.pack()                      # packing the textbox for student name   
mobilenum.pack()                     # packing the mobile number label in the mainframe
mobilenumtext.pack()                # packing the text box for the mobile number in the mainframe
email_id.pack()                    # packing the email id label inside the mainframe
email_idbox.pack()                  # packing the text box for the email inside the mainframe
homeaddress.pack()                # packing the homeaddress label inside the mainframe
homeaddressbox.pack()             # packing the homeaddress textbox inside the mainframe
gender.pack()                    # packing the gender label inside the mainframe
genderdrop.pack()                 # packing the gender dropdowm menu to select from
coursesenrolled.pack()           # packing the courses label in the mainframe

# packing all the radio buttons
course_rd1.pack()             
course_rd2.pack()             
course_rd3.pack()             
course_rd4.pack()    

languages.pack()                    # packing the languages label inside the mainframe

# packing all the checkboxes
checkbox1.pack()
checkbox2.pack()
checkbox3.pack()

rates.pack()                       # packing the communication skills rating message
progressmeter.pack()               # packing the progress meter

  
# using the mainloop function to run the window, loops the program unlimited number of times, until inturepted by anything
app.mainloop()