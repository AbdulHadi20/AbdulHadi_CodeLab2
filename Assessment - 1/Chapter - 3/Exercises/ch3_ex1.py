"""
Chapter 3 : Exerxise 1 : Greeting App 

Develop a GUI to greet the user. The app should have two frames: InputFrame and DisplayFrame.
In InputFrame, include the following:

- A title label in blue.
- An entry field for the user's name.
- A dropdown menu for selecting a color.
- An "Update Greeting" button.
- In DisplayFrame, include a label to display the personalized greeting.
- Initially, DisplayFrame is empty, when the user clicks the "Update Greeting" button in InputFrame, the personalized greeting should appear in DisplayFrame with the selected color.
- Use different background colors for each frame.

"""

# start of the program

# importing the required modules
from tkinter import *
from tkinter import ttk # for styling (theme tkinter)

# initializing the root window
appwindow = Tk()

# setting the dimensions, title, resizing, etc. 
appwindow.title("Greeting App")
appwindow.geometry("800x400")
appwindow.resizable(0, 0)
appwindow.configure(background = 'gray')

############################## CREATING THE REQUIRED FUNCTIONS #########################################

# creating the function to change the color of the background based on the selected  color
def update_display():
    selected_color = colors_select.get()
    greet_person_str.set(f"Hi {entry_name.get()}! \n Your favorite color is {selected_color}")
    
    greet_person.pack(side = TOP, anchor = N, padx = 30, pady = 30)
    greet_person.configure(background = selected_color)

    displayframe.configure(background = selected_color)

# creating a function to clear the entry widget
def clear():
    entry_name.delete(0, "end")
    thecolormenu.set(dropdown_list[0])
    displayframe.configure(background = 'white')
    greet_person.configure(background = 'white')
    greet_person_str.set("")
    

############################## CREATING THE REQUIRED WIDGETS #########################################

# creating a title label
title = Label(appwindow, font = ('Roboto', 18, 'bold'), text = "GREETING APP", bg = 'gray', fg = 'blue') 

# creating a frame for input and display
inputframe = LabelFrame(appwindow, bg = 'white', border = 0)
displayframe = LabelFrame(appwindow, bg = 'white', border = 0)

# creating a label and entry widget for the user to read and type
label_name = Label(inputframe, font = ('Roboto', 14), text = "Please Enter your name = ", bg = 'white')
entry_name = Entry(inputframe, width = 15, font = ('Roboto', 14), border = 0, bg = 'gray')

# creating a label to tell the user to select from the dropdown menu
optn_menu_label = Label(inputframe, font = ('Roboto', 14), text = "Please Select from the dropdown menu = ", bg = 'white')

# creating a dropdown menu list
colors_select = StringVar()
dropdown_list = ['Select Color','red', 'orange', 'green', 'blue', 'purple', 'black']
colors_select.set(dropdown_list[0])

# styling the dropdown list with ttk
optionmenu_style = ttk.Style()
optionmenu_style.configure("TCombobox", font = ('Roboto', 12), background = 'white')

thecolormenu = ttk.Combobox(inputframe, textvariable = colors_select, values = dropdown_list, style = "TCombobox")

# creating a button to update greeting
update_greet = Button(inputframe, text = "Update Greeting", font = ('Arial', 13), bg = 'black', fg = 'white', padx = 5, pady = 5, command = update_display)

# creating a button to clear out the entry labels
clearbtn = Button(inputframe, text = "Clear", font = ('Arial', 13), bg = 'black', fg = 'white', padx = 5, pady = 5, command = clear)


# creating a label for personalized greeting
greet_person_str = StringVar()
greet_person = Label(displayframe, textvariable = greet_person_str)

############################## DISPLAYING THE REQUIRED WIDGETS #########################################

title.pack(side = TOP, anchor = N, padx = 10, pady = 10)                                     # displaying the title
inputframe.pack(side = LEFT, anchor = W, padx = 10, pady = 10, fill = BOTH, expand = 1)      # displaying the input frame
displayframe.pack(side = RIGHT, anchor = E, padx = 10, pady = 10, fill = BOTH, expand = 1)   # displaying the display frame
label_name.pack(pady = 5)                                                                    # displaying the label for the name
entry_name.pack(pady = 5)                                                                    # displaying the entry widgets
optn_menu_label.pack(pady = 5)                                                               # displaying the dropdown menu label
thecolormenu.pack(pady = 5)                                                                  # displaying the dropdown menu
update_greet.pack(pady = 10)                                                                 # displaying the update greeting button
clearbtn.pack(pady = 10)                                                                     # displaying the clear button
 
# running the root window
appwindow.mainloop()

# end of the program