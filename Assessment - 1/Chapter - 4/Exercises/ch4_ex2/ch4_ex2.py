"""
Chapter 4 : Exercise 2 : Count String

The file sentences.txt has a list of string data. Develop a GUI App that finds out how many times the following string appears

- Hello my name is Peter Parker
- I love Python Programming
- Love
- Enemy

"""

# starting of the program

# importing the required modules
from tkinter import *
import os

# initializing the root window and customizing its appearance

root = Tk()                                        # creates a root window
root.title("Count String")                         # sets the title of the window
root.geometry("500x500")                           # sets the dimension of the window
root.resizable(0, 0)                               # disables the resizing of the window
root.configure(background = 'orange')              # sets the background color of the window

############################ CREATING THE REQUIRED FUNCTIONS #############################################

def read_file():

    with open("sentences.txt", 'r') as file:
        content = file.read()

        # creating the label to display the results
        result_label_str = StringVar()
        result_label = Label(root, textvariable = result_label_str,font = ('Arial', 18), bg = 'orange')
        result_label.pack(pady = 10)

        result_label_str.set(f"The data in the file 'sentences.txt' is: \n {content}")
        
        # counting the occurence of each string
        
        


############################ CREATING & DISPLAYING THE REQUIRED WIDGETS #############################################

# creating a label for the heading
heading_label = Label(root, font = ('Arial', 25, 'bold'), text = "Read File", bg = 'orange')
heading_label.pack(side = TOP, pady = 10)

# creating a button to read data in a txt file
read_data = Button(root, font = ('Arial', 18), text = "Read Data", bg = 'green', padx = 5, pady = 5, command = read_file)
read_data.pack(padx = 35, pady = 20)

ans_label_str = StringVar()
ans_label = Label(root, font = ('Arial', 16, 'bold'), bg = 'orange', textvariable = ans_label_str)
ans_label.pack(pady = 30)

# running the main root window
root.mainloop()

# end of the program