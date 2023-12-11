"""
Chapter 3 : Exercise 2 : Coffee Vending Machine

Develop a coffee Vending Machine that asks users to select the type of coffee, and also prompts users to select various options like 
sugar, milk, etc. Once selected display the message using a message box. Also, use images in the app.  

Extension :
Add other features to the previous app such as handling money.

"""

# start of the program

# importing the required modules (libraries)

from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import os
from tkinter import ttk

# initializing the root window
window = tk.Tk()

# setting the dimensions, title, etc. 
window.title("Coffee Vending Machine")
window.geometry("480x760")
window.resizable(0, 0)
window.configure(background = '#6f4e37')

################################# CREATING & DISPLAYING THE REQUIRED WIDGETS ##########################################

# creating a heading label and displaying it
heading = Label(window, font = ('Roboto', 25, 'bold'), text = "Coffee Vending Machine", bg = '#6f4e37', fg = '#ffffff')
heading.pack(pady = 10)


# creating tabs
tabs = ttk.Notebook(window)

# creating frames for the different tabs
tab1 = Frame(tabs, width = 480, height = 700, bg = '#6f4e37')
tab2 = Frame(tabs, width = 480, height = 700, bg = '#6f4e37')
tab3 = Frame(tabs, width = 480, height = 700, bg = '#6f4e37')
tab4 = Frame(tabs, width = 480, height = 700, bg = '#6f4e37')

# adding frames in the tabs
tabs.add(tab1, text = 'Welcome')
tabs.add(tab2, text = 'Select Coffee')
tabs.add(tab3, text = 'Add-ons')
tabs.add(tab4, text = 'Checkout')
tabs.pack(fill = X, expand = 1, anchor = S)

################################# CREATING & DISPLAYING THE HOME TAB ##########################################

# creating a heading for the first page
heading_welcome = Label(tab1, font = ('Roboto', 18, 'bold'), text = "Welcome! Please select your coffee.", bg = '#6f4e37', fg = '#ffffff').pack(pady = 50)

# creating a frame for the latte coffee
latte_frame = LabelFrame(tab1, width = 400, height = 150, border = 0, bg = '#363636').pack(pady = 20)

# placing the image, label, price, and selection button inside the frame
file_path = os.path.dirname(os.path.realpath(__file__))             # a var with the file path 
latte_dir = Image.open(os.path.join(file_path, "latte.png"))        #  creating an image, and calling the file path and image file name
latte_img = ImageTk.PhotoImage(latte_dir)                           # this makes the image widget, and calls the img var 



# running the main window
window.mainloop()