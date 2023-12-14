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
from tkinter import messagebox

# initializing the root window and customizing its appearance

root = Tk()                                        # creates a root window
root.title("Count String")                         # sets the title of the window
root.geometry("500x500")                           # sets the dimension of the window
root.resizable(0, 0)                               # disables the resizing of the window
root.configure(background = 'orange')              # sets the background color of the window

############################ CREATING THE REQUIRED FUNCTIONS #############################################

# creating a function that counts the occurences of a string in a file
def read_file(string, file_path):
    # using try/except to handle errors better
    try:
        # opening the file 
        with open('sentences.txt', 'r') as file:
            content = file.read()           # reads the conent in the file

            # counting the strings
            count = content.lower().count(string.lower())

            # getting the result
            ans_label_str.set(f'The string {string} appears {count} times\n')
    
    except:
        messagebox.showerror("ERROR", 'File not found or does not exist')

# creating a function for the button
def submit_btn():
    # creating a list of strings to search for
    strings = [
        'Hello my name is Peter Parker', 'I love Python Programming', 'Love', 'Enemy'
    ]


    ans = ""
    # creating a for loop to go through each line in file
    for string in strings:
        ans = read_file(string, 'sentences.txt') + '\n'
        ans_label.config(text = ans)


############################ CREATING & DISPLAYING THE REQUIRED WIDGETS #############################################

# creating a label for the heading
heading_label = Label(root, font = ('Arial', 25, 'bold'), text = "Read File", bg = 'orange')
heading_label.pack(side = TOP, pady = 10)

# creating a button to read data in a txt file
read_data = Button(root, font = ('Arial', 18), text = "Read Data", bg = 'green', padx = 5, pady = 5, command = submit_btn)
read_data.pack(padx = 35, pady = 20)

ans_label_str = StringVar()
ans_label = Label(root, font = ('Arial', 10, 'bold'), bg = 'orange', textvariable = ans_label_str)
ans_label.pack(pady = 30)

# running the main root window
root.mainloop()

# end of the program