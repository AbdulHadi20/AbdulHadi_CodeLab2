"""
Chapter 6 : Exercise 4 : Line Graph

Draw a line in a diagram from position (1, 2) to position (6, 8)
Draw a dotted line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10)

"""

# start of the program

# importing the required modules/libraries 
from tkinter import *

# initializing the root window
app = Tk()                                    # sets the root window
app.title('Line Graph Exercise')              # sets the title of the window
app.geometry("600x600")                       # disables the resizing
app.resizable(0, 0)
app.configure(background = 'gray')

######################################### CREATING & DISPLAYING THE REQUIRED WIDGETS #########################################

# creating a heading widget
heading = Label(app, text = "Line Graph", font = ('Sans Serif', 20, 'bold'), bg = 'gray')
heading.pack(pady = 10)

# creating a blank canvas
canvas_art = Canvas(app, width = 500, height = 450)
canvas_art.pack()

# drawing the first line, from pos(1, 2) to (6, 8)
canvas_art.create_line(100, 100, 500, 450, fill = 'pink', width = 4)

# drawing the second line from pos (1, 2, 3, 4, 5, 6, 7 , 8)
canvas_art.create_line(100, 100, 300, 250, 400, 500, 400, 450, fill = 'purple', width = 5, dash=(2, 2))

# running the main window (mainloop)
app.mainloop()

# end of program