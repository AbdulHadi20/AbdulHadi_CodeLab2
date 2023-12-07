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
window.geometry("800x400")
window.resizable(0, 0)
window.configure(background = 'beige')


################################ CREATING THE FUNCTIONS FOR THE BUTTONS ###############################################

def far_to_cel():

    temp_farenheit = userinput_entry.get()  # saving the the user's value in a variable

    # formula to convert from farenheit to celcius
    temp = (float(temp_farenheit) - 32) * 5 / 9

    temp_ans.set(f"\n The temperature {temp_farenheit} is converted to Celcius, which is = {temp}") # displays the result

def cel_to_far():

    temp_celcius = userinput_entry.get()  # saving the the user's value in a variable

    # formula to convert from celcius to farenheit
    temp = (float(temp_celcius) * 9 / 5) + 32

    temp_ans.set(f"\n The temperature {temp_celcius} is converted to Celcius, which is = {temp}") # displays the result

def delete_entry():
    userinput_entry.delete(0, "end")
############################# CREATING WIDGETS ########################################################################

# creating a heading label
heading = Label(window, font = ('Helavatica', 28, 'bold'), text = "Welcome to the Temperature Converter !", bg = 'beige')

# creating a label to ask the user if they want to convert from CELCIUS to FARENHEIT or vice versa
selection = Label(window, font = ('Roboto', 16), text = "Please select from the available options...", bg = 'beige')

# creating a frame to set the the buttons
btns_frame = LabelFrame(window, border = 0, bg = 'beige')
# creating two buttons for the options
f_to_c = Button(btns_frame, font = ('Roboto', 13), text = "Farenheit to Celcius", bg = 'lightgreen', border = 3, command = far_to_cel)
c_to_f = Button(btns_frame, font = ('Roboto', 13), text = "Celcius to Farenheit", bg = 'lightgreen', border = 3, command = cel_to_far)

# creating a frame for the question and answers
innerframe = LabelFrame(window, border = 0, bg = 'beige')

# creating a label for for the message to ask the user to enter the temperature in farenheit
userinput_label = Label(innerframe, font = ('Arial', 14, 'bold'), text = "Please Enter the temeperature = ", bg = 'beige')

# an entry widget for the farenheit temperature
userinput_entry = Entry(innerframe, width = 25, font = ('Arial', 12))

# creating a label to display the result
temp_ans = StringVar()
temp = Label(window, textvariable = temp_ans, font = ('Roboto', 13, 'bold'), bg = 'beige')

# creating a button to clear out the entry of the user
clear = Button(window, font = ('Roboto', 13), bg = 'red', text = "Clear", fg = 'white', command = delete_entry)

############################ DISPLAYING THE WIDGETS IN THE WINDOW ######################################################

heading.pack(side = TOP, padx = 5, pady = 10)                # displays the man heading labe;
selection.pack(side = TOP, padx = 5, pady = 10)              # displays the text for instructions
btns_frame.pack(side = TOP, padx = 5, pady = 10)             # displays the frame for the buttone
f_to_c.grid(row = 0, column = 0, padx = 20)                  # displays the button for farenheit to celcius conversion
c_to_f.grid(row = 0, column = 1, padx = 20)                  # displays the button for celcius to farenheir conversion
innerframe.pack(side = TOP, padx = 5, pady = 10)             # displays the frame for getting the user's values and labels
userinput_label.grid(row = 0, column = 0)                    # displays teh label that asks the temperature from the user
userinput_entry.grid(row = 0, column = 1)                    # displays the entry widget for the user to enter
clear.pack(side = TOP, padx = 5, pady = 20)                  # displays the button for clearing out the entry widegt
temp.pack(side = BOTTOM, anchor = S, padx = 5, pady = 30)    # displays teh result after the conversion has been completed

# running the main window
window.mainloop()

# end of the program