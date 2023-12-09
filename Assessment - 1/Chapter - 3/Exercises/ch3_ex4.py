"""
Chapter 3 : Exercise 4 : Draw Shape

Using tkinter module develop Gui to ask the user to select shapes like oval, rectangle, square, and triangle and draw the shape 
using canvas.  

Extension
Ask the user to input the coordinate values of the selected option

"""

# start of the program

# importing the required modules
import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

# initializing the root window
root = tk.Tk()

# setting the dimensions, title, etc.
root.title("Draw Shape")          # sets the title
root.geometry("800x700")         # sets the width and height
root.resizable(0, 0)              # sets the resizing options
root.config(bg = 'black')         # sets the background color

########################### CREATING THE REQUIRED FUNCTIONS ######################################

# creating a function to draw a shape
def shape_draw(shape, coords_shape):
    if shape == 'triangle':
        shape_canvas.create_polygon(coords_shape, fill = 'red')

    elif shape == 'rectangle':
        shape_canvas.create_rectangle(coords_shape, fill = 'blue')

    elif shape == 'circle':
        shape_canvas.create_oval(coords_shape, fill = 'green')

    elif shape == 'square':
        shape_canvas.create_rectangle(coords_shape, fill = 'brown')

# creating a function to get the coordinates of the shape based on the shape selection
def coords(*args):
    shape = shape_selected.get()

    if shape == "Select Shape":
        coords_label.config(text = "Enter the Co-ordinates")

    elif shape == 'triangle':
        coords_label.config(text = "Enter coordinates for the triangle (x1 y1 x2 y2 x3 y3)= ")

    else:
        coords_label.config(text = f"Enter the Co-ordinates for {shape} (x1 y1 x2 y2) = ")

def co_ordinates_get():
    shape = shape_selected.get()

    if shape_draw == 'Select Shape':
        return
    
    coords_shape = coords_entry.get()
    
    if not coords_shape:
        return
    
    coordinates = [int(coord) for coord in coords_shape.split()]

    shape_draw(shape, coordinates)




########################### CREATING THE REQUIRED WIDGETS ######################################

# creating a heading label
head = tk.Label(root, font = ('Arial', 18, 'bold'), text = "Welcome to the shape maker !", fg = 'white', padx = 5, pady = 5, bg = 'black')

# creating a frame for the label and dropdown menu
mainframe = tk.LabelFrame(root, border = 0)

# creating a label and dropdowm menu for user to tell what shape to draw
label = tk.Label(mainframe, font = ('Roboto', 14), bg = 'black', fg = 'white', text = "Select the shape you wish to draw: ")

# list of shapes 
shapes_list = ['Select Shape', 'circle', 'square', 'rectangle', 'triangle']
shape_selected =tk.StringVar()
shape_selected.set(shapes_list[0])
shape_selected.trace_add("write", coords)

# shape combobox
combobox_shape = Combobox(mainframe, textvariable = shape_selected, values = shapes_list, width = 50)


# creating a canvas to draw a shape
shape_canvas = tk.Canvas(root, width = 400, height = 400, bg = 'white')

# creating a label and entry to enter coords
coords_label = tk.Label(root, font = ('Roboto', 14), bg = 'black', fg = 'white', text = "Please Enter the Coordinates = ")
coords_entry = tk.Entry(root, width = 50, border = 0, font = ('Roboto', 14))

# creating a button to submit the shape coordinates
shape_btn = tk.Button(root, font = ('Roboto', 16), text = "Draw Shape", bg = 'green', fg = 'white', command = co_ordinates_get)

########################### DISPLAYING THE REQUIRED WIDGETS ######################################

head.pack(side = TOP, anchor = N, padx = 10, pady = 10)              # displays the heading
mainframe.pack(side = TOP)                                           # displays the mainframe for the label and dropdown menu
label.grid(row = 0, column = 0, padx = 30, pady = 10)                # displays the label in the mainframe
combobox_shape.grid(row = 0, column = 1, padx = 30, pady = 10)       # displays the dropdown menu in the mainframe
shape_canvas.pack(pady = 10)                                         # displays the canvas 
coords_label.pack(pady = 10)                                         # displays the coords label
coords_entry.pack(pady = 10)                                         # displays the entry to write coords
shape_btn.pack(pady = 10)                                            # displays the button 


# running the main window (mainloop)
root.mainloop()

# end of the program