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


# initializing the root window
window = tk.Tk()

# setting the dimensions, title, etc. 
window.title("Coffee Vending Machine")
window.geometry("480x760")
window.resizable(0, 0)
window.configure(background = 'beige')

################################# CREAtING & DISPLAYING THE REQUIRED WIDGETS ##########################################




# running the main window
window.mainloop()