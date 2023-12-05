"""
Chapter 2 : Exercise A : Temperature Converter

Writing a program that develops a GUI application using tkinter, allowing users to convert between Celcius and Farenheit

"""

# start of the program


# importing the tkinter module library
from tkinter import *

# creating a root window, setting the dimensions, background color, and window resizable options 
window = Tk() 
window.title("Temperature Converter")
window.geometry("800x600")
window.resizable(0, 0)
window.configure(background = 'beige')


################################ CREATING THE FUNCTIONS FOR THE BUTTONS ###############################################

def far_to_cel():
    temp_farenheit = farenheittemp.get()


############################# CREATING WIDGETS ########################################################################

# creating a heading label
heading = Label(window, font = ('Helavatica', 28, 'bold'), text = "Welcome to the Temperature Converter !", bg = 'beige')

# creating a label to ask the user if they want to convert from CELCIUS to FARENHEIT or vice versa
selection = Label(window, font = ('Roboto', 16), text = "Please select from the available options...", bg = 'beige')

# creating a frame to set the the buttons
btns_frame = LabelFrame(window, border = 0, bg = 'beige')
# creating two buttons for the options
f_to_c = Button(btns_frame, font = ('Roboto', 13), text = "Farenheit to Celcius", bg = 'lightgreen', border = 3)
c_to_f = Button(btns_frame, font = ('Roboto', 13), text = "Celcius to Farenheit", bg = 'lightgreen', border = 3)

# creating a label 

############################ DISPLAYING THE WIDGETS IN THE WINDOW ######################################################

heading.pack(side = TOP, padx = 5, pady = 10)
selection.pack(side = TOP, padx = 5, pady = 10)
btns_frame.pack(side = TOP, padx = 5, pady = 10)
f_to_c.grid(row = 0, column = 0, padx = 20) 
c_to_f.grid(row = 0, column = 1, padx = 20) 




# running the main window

window.mainloop()