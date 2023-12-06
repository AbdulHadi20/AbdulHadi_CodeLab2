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

    # packing the widgets required for the farenheit temperature calculations
    farenheittemp_label.grid(row = 0, column = 0)
    farenheittemp_entry.grid(row = 0, column = 1)
    
    temp_farenheit = farenheittemp_entry.get()  # saving the the user's value in a variable

    # formula to convert from farenheit to celcius
    temp = (temp_farenheit - 32) * 5 / 9

    temp_ans.set(f"\n The temperature {temp_farenheit} is converted to Celcius, which is = {temp}").grid(row = 1, column = 0, padx = 20)

############################# CREATING WIDGETS ########################################################################

# creating a heading label
heading = Label(window, font = ('Helavatica', 28, 'bold'), text = "Welcome to the Temperature Converter !", bg = 'beige')

# creating a label to ask the user if they want to convert from CELCIUS to FARENHEIT or vice versa
selection = Label(window, font = ('Roboto', 16), text = "Please select from the available options...", bg = 'beige')

# creating a frame to set the the buttons
btns_frame = LabelFrame(window, border = 0, bg = 'beige')
# creating two buttons for the options
f_to_c = Button(btns_frame, font = ('Roboto', 13), text = "Farenheit to Celcius", bg = 'lightgreen', border = 3, command = far_to_cel)
c_to_f = Button(btns_frame, font = ('Roboto', 13), text = "Celcius to Farenheit", bg = 'lightgreen', border = 3)

# creating a frame for the question and answers
innerframe = LabelFrame(window, border = 0, bg = 'beige')

# creating a label for for the message to ask the user to enter the temperature in farenheit
farenheittemp_label = Label(innerframe, font = ('Arial', 14, 'bold'), text = "Please Enter the temeperature in farenheit = ")

# an entry widget for the farenheit temperature
farenheittemp_entry = Entry(innerframe, width = 25, font = ('Arial', 12))

# creating a label to display the result
temp_ans = StringVar()
temp = Label(innerframe, textvariable = temp_ans)


############################ DISPLAYING THE WIDGETS IN THE WINDOW ######################################################

heading.pack(side = TOP, padx = 5, pady = 10)
selection.pack(side = TOP, padx = 5, pady = 10)
btns_frame.pack(side = TOP, padx = 5, pady = 10)
f_to_c.grid(row = 0, column = 0, padx = 20) 
c_to_f.grid(row = 0, column = 1, padx = 20) 
innerframe.pack(side = TOP, padx = 5, pady = 10)




# running the main window

window.mainloop()