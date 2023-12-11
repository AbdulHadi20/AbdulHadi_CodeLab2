"""
Chapter 3 : Exercise A : BurgerShack Vendor

Burger Shack is about to open in RAK, however, the fast food chain is in need of an ordering system. Write a program to handle 
the ordering process for the burger shack. The program should include:

- The ability to choose between at least three burger types (e.g. Beef, Chicken, Vegetarian)
- The ability to add toppings, with at least three to choose from (e.g. cheese, peanut butter, avocado)
- The ability to add condiments, with at least three to choose from (e.g. ketchup, mayonnaise, bbq sauce)
- The ability to add sides, these can include items such as fries and drinks.
- The ability to handle payment and return change to the user
- You should design your program to make use of functions and pass information to and from these as appropriate. 

Alongside the above requirements, you are free to extend the functionality of the program as you see fit.

"""
# start of the program

# importing the required modules/libraries
from tkinter import *
from tkinter import ttk
import tkinter as tk

# initializing the root window
app = Tk()

# setting the tite, geometry, background, etc. 
app.title("BurgerShack Vendor")                      # sets the title
app.geometry("600x600")                              # sets the dimensions
app.resizable(0, 0)                                  # sets the window size to be fixed
app.configure(background = 'orange')                 # sets the backgroun color

# creating and packing the heading label
heading = Label(app, font = ('Comic Sans Ms', 30, 'bold'), text = "BurgerShack Vendor", fg = 'white', bg = 'orange')
heading.pack(pady = 20)


# creating tabs
tabs = ttk.Notebook(app)

# creating frames for the tabs
frame1 = Frame(tabs, width = 600, height = 500, bg = 'red')
frame2 = Frame(tabs, width = 600, height = 500, bg = 'red')
frame3 = Frame(tabs, width = 600, height = 500, bg = 'cyan')
frame4 = Frame(tabs, width = 600, height = 500, bg = 'cyan')
frame5 = Frame(tabs, width = 600, height = 500, bg = 'cyan')

# adding the frames in the tab
tabs.add(frame1, text = 'Welcome')
tabs.add(frame2, text = 'Select Burger')
tabs.add(frame3, text = 'Add Toppings & Stuff')
tabs.add(frame4, text = 'Add Side Dishes')
tabs.add(frame5, text = 'Checkout')
tabs.pack(fill = BOTH, expand = 1)

# creating functions to go to the frame1
def next_frame(*args):
    frames = [frame1, frame2, frame3, frame4, frame5]

    for frame in frames:
        frame1.destroy()

# creating functions to go to the frame2    
def next_frame1(*args):
    frame2.destroy()


######################## CREATING AND DISPLAYING WIDGETS IN THE WELCOME TAB ############################

# creating a label to greet the user and displaying it
greet_label = Label(frame1, font = ('Comic Sans Ms', 25, 'bold'), text = "Welcome to BurgerShack!", fg = 'white', bg = 'red').pack(pady = 10)

# adding a burger image

# creating a button to go to the next page and displaying it
nextpage_btn = Button(frame1, font = ('Arial', 20), text = "Start My Order", bg = 'yellow', padx = 5, pady = 5, command = lambda: next_frame())
nextpage_btn.pack(pady = 10, anchor = S, side = BOTTOM)

######################## CREATING AND DISPLAYING WIDGETS IN THE SELECT BURGER TAB ############################

# creating a heading for the select burger frame
selectburger_label = Label(frame2, font = ('Comic Sans Ms', 25, 'bold'), text = "Select your Burger", fg = 'white', bg = 'red').pack(pady = 10)

# # creating the label for the chicken burger
# chicken_burger_label = Label(frame2, font = ('Arial', 18), text = "Chicken Burger - AED 10", fg = 'white', bg = 'red')
# chicken_burger_label.pack(pady = 20, side = LEFT, padx = 40, anchor = NW)

# creating a button to select the chicken burger
chicken_select = Button(frame2, font = ('Arial', 18, 'bold'), text = "CHICKEN BURGER - AED 15", bg = 'green', padx = 20, pady = 5, border = 10, command = lambda: next_frame1())
chicken_select.pack(pady = 20)

# creating a button to select the beef burger
beef_select = Button(frame2, font = ('Arial', 18, 'bold'), text = "BEEF BURGER - AED 20", bg = 'green', padx = 20, pady = 5, border = 10, command = lambda: next_frame1())
beef_select.pack(pady = 20)

# creating a button to select the vegetarian burger
veg_select = Button(frame2, font = ('Arial', 18, 'bold'), text = "VEGETRIAN BURGER - AED 10", bg = 'green', padx = 20, pady = 5, border = 10, command = lambda: next_frame1())
veg_select.pack(pady = 20)




# running the main window
app.mainloop()