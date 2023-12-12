"""
Chapter 3 : Exercise 3 : Area Function

Develop a GUI application using tkinter that allows users to calculate and display the areas of various shapes, 
including circles, squares, and rectangles. The application should utilize a tabbed interface to organize the 
calculations for each shape. Each of the 3 functions should ask for the necessary information (e.g. lengths 
and/or angles and output the answer.

"""

# start of the program

# importing the required modules
from tkinter import *
from tkinter import ttk


# initializing the root window
app = Tk()

# setting the dimensions, title, etc.
app.title("Area Function")           # sets the title
app.geometry("800x700")              # sets the dimensions (width & height)
app.resizable(0, 0)                  # sets the resizing to false
app.configure(background = 'pink')   # sets the background color

########################## CREATING THE REQUIRED WIDGETS ####################################

# creating the heading tag
heading_label = Label(app, font = ('Helavatica', 20, 'bold'), text = "Shape Area Calculator", bg = 'pink', fg = 'gray')
heading_label.pack(side = TOP, pady = 10)

# creating a notebook(tabs)
notebook = ttk.Notebook(app)

# creating frames for each tab
frame1 = Frame(notebook, width = 800, height = 500, bg = 'skyblue')  # frame for the rectangle tab
frame2 = Frame(notebook, width = 800, height = 500, bg = 'green')  # frame for the square tab
frame3 = Frame(notebook, width = 800, height = 500, bg = 'yellow')  # frame for the circle tab
frame4 = Frame(notebook, width = 800, height = 500, bg = 'orange')  # frame for the triangle tab

# adding the tabs in the frames
notebook.add(frame1, text = "Rectangle")
notebook.add(frame2, text = "Square")
notebook.add(frame3, text = "Circle")
notebook.add(frame4, text = "Triangle")
notebook.pack(fill = X, expand = 1, anchor = S)

def clear_entry():
    length_entry.delete(0, "end")
    width_entry.delete(0, "end")
    radius_entry.delete(0, "end")
    base_entry.delete(0, "end")
    height_entry.delete(0, "end")

########################## CREATING, CALCULATING, & DISPLAYING THE RECTANGLE TAB ####################################

# creating the calculation function
def calculate_rect():
    rec_length = length_entry.get()
    rec_width = width_entry.get()

    if rec_length.isdigit() and rec_width.isdigit():
        length = float(rec_length)
        width = float(rec_width)

        area_rect = length * width

        result_str.set(f"The area of the rectangle is {area_rect} m.sq") 
        
# creating a heading for the rectangle tab and packing it
rect_head = Label(frame1, font = ('Arial', 20, 'bold'), text = "RECTANGLE AREA CALCULATOR", bg = 'skyblue')
rect_head.grid(row = 0, column = 0, columnspan = 30, pady = 40, padx = 150)

# creating the label for asking the length and width
length_rect = Label(frame1, font = ('Arial', 14), text = "Enter the length = ", bg = 'skyblue').grid(row = 1, column = 0, padx = 5, pady = 10) 
width_rect = Label(frame1, font = ('Arial', 14), text = "Enter the width = ", bg = 'skyblue').grid(row = 2, column = 0, padx = 5, pady = 10) 

# creating the entry widgets for the length and width
length_entry = Entry(frame1, width = 20, font = ('Arial', 14))
length_entry.grid(row = 1, column = 1)

width_entry = Entry(frame1, width = 20, font = ('Arial', 14))
width_entry.grid(row = 2, column = 1)

# creating buttons for starting the calculations & clearing
calc_btn = Button(frame1, bg = 'darkgray', fg = 'white', text = "Calculate", command = calculate_rect).grid(row = 2, column = 2)
clear_btn = Button(frame1, bg = 'darkgray', fg = 'white', text = "Clear", command = clear_entry).grid(row = 1, column = 2)

# displaying the result
result_str = StringVar()
result = Label(frame1, font = ('Arial', 16), textvariable = result_str, bg = 'skyblue').grid(row = 5, column = 0, columnspan = 10, padx = 150, pady = 10)

########################## CREATING, CALCULATING, & DISPLAYING THE SQUARE TABS ####################################

# creating the calculation function
def calculate_sq():
    sq_length = length_entry.get()

    if sq_length.isdigit():
        length = float(sq_length)

        area_sq = length * length

        result_str.set(f"The area of the square is {area_sq} m.sq")

# creating a heading for the square tab and packing it
sq_head = Label(frame2, font = ('Arial', 20, 'bold'), text = "SQUARE AREA CALCULATOR", bg = 'green')
sq_head.grid(row = 0, column = 0, columnspan = 30, pady = 40, padx = 150)

# creating the label for asking the length of the side
length_sq = Label(frame2, font = ('Arial', 14), text = "Enter the length = ", bg = 'green').grid(row = 1, column = 0, padx = 5, pady = 10)  

# creating the entry widgets for the length of the side
length_entry = Entry(frame2, width = 20, font = ('Arial', 14))
length_entry.grid(row = 1, column = 1)

# creating buttons for starting the calculations & clearing
calc_btn = Button(frame2, bg = 'darkgray', fg = 'white', text = "Calculate", command = calculate_sq).grid(row = 1, column = 3)
clear_btn = Button(frame2, bg = 'darkgray', fg = 'white', text = "Clear", command = clear_entry).grid(row = 1, column = 2)

# displaying the result
result_str = StringVar()
result = Label(frame2, font = ('Arial', 16), textvariable = result_str, bg = 'green').grid(row = 5, column = 0, columnspan = 10, padx = 150, pady = 50)

########################## CREATING, CALCULATING, & DISPLAYING THE CIRCLE TABS ####################################

# creating the calculation function
def calculate_circ():
    circ_radius = radius_entry.get()

    if circ_radius.isdigit():
        radius = float(circ_radius)
 
        area_circ = 3.14 * radius**2

        result_str.set(f"The area of the circle is {area_circ} m.sq")

# creating a heading for the circle tab and packing it
circ_head = Label(frame3, font = ('Arial', 20, 'bold'), text = "CIRCLE AREA CALCULATOR", bg = 'yellow')
circ_head.grid(row = 0, column = 0, columnspan = 30, pady = 40, padx = 150)

# creating the label for asking the radius of the circle
radius_circ = Label(frame3, font = ('Arial', 14), text = "Enter the radius = ", bg = 'yellow').grid(row = 1, column = 0, padx = 5, pady = 10)  

# creating the entry widgets for the radius of the circle
radius_entry = Entry(frame3, width = 20, font = ('Arial', 14))
radius_entry.grid(row = 1, column = 1)

# creating buttons for starting the calculations & clearing
calc_btn = Button(frame3, bg = 'darkgray', fg = 'white', text = "Calculate", command = calculate_circ).grid(row = 1, column = 3)
clear_btn = Button(frame3, bg = 'darkgray', fg = 'white', text = "Clear", command = clear_entry).grid(row = 1, column = 2)

# displaying the result
result_str = StringVar()
result = Label(frame3, font = ('Arial', 16), textvariable = result_str, bg = 'yellow').grid(row = 5, column = 0, columnspan = 10, padx = 150, pady = 50)

########################## CREATING, CALCULATING, & DISPLAYING THE TRIANGLE TABS ####################################

# creating the calculation function
def calculate_tri():
    tri_base = base_entry.get()
    tri_height = height_entry.get()

    if tri_base.isdigit() and tri_height.isdigit():
        base = float(tri_base)
        height = float(tri_height)

        area_tri = 0.5 * (base * height)

        result_str.set(f"The area of the triangle is {area_tri} m.sq")

# creating a heading for the rectangle tab and packing it
tri_head = Label(frame4, font = ('Arial', 20, 'bold'), text = "TRIANGLE AREA CALCULATOR", bg = 'orange')
tri_head.grid(row = 0, column = 0, columnspan = 30, pady = 40, padx = 150)

# creating the label for asking the length and width
base_tri = Label(frame4, font = ('Arial', 14), text = "Enter the base = ", bg = 'orange').grid(row = 1, column = 0, padx = 5, pady = 10) 
height_tri = Label(frame4, font = ('Arial', 14), text = "Enter the height = ", bg = 'orange').grid(row = 2, column = 0, padx = 5, pady = 10) 

# creating the entry widgets for the length and width
base_entry = Entry(frame4, width = 20, font = ('Arial', 14))
base_entry.grid(row = 1, column = 1)

height_entry = Entry(frame4, width = 20, font = ('Arial', 14))
height_entry.grid(row = 2, column = 1)

# creating buttons for starting the calculations & clearing
calc_btn = Button(frame4, bg = 'darkgray', fg = 'white', text = "Calculate", command = calculate_tri).grid(row = 2, column = 2)
clear_btn = Button(frame4, bg = 'darkgray', fg = 'white', text = "Clear", command = clear_entry).grid(row = 1, column = 2)

# displaying the result
result_str = StringVar()
result = Label(frame4, font = ('Arial', 16), textvariable = result_str, bg = 'orange').grid(row = 5, column = 0, columnspan = 10, padx = 150, pady = 50)

# running the main window
app.mainloop()


# end of the program