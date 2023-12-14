"""
Chapter 4 : Exercise 4 : Letter Count

Develop a GUI App that asks the user to enter a character, reads the contents of the sentences.txt file, 
and counts the occurrences of the letter.

"""

# start of the program

# importing the required lirbaries/modules
from tkinter import *
from tkinter import messagebox

# initializing the root window
root = Tk()

# setting the dimensions, title, etc.
root.title("Letter Count")                  # sets the title
root.geometry("400x300")                    # sets the dimensions
root.configure(background = 'blue')         # sets the background color
root.resizable(0, 0)                        # disables the resizing

############################## CREATING THE REQUIRED FUNCTIONS ####################################

# creating a function that counts the occcurences of the word in the file
def count_occurrences(character, file_path):
    # using try / except for error handling
    try:
        # opening and reading the 'sentences.txt' file, read only
        with open('sentences.txt', 'r') as file:
            content = file.read()
            # checking the count of words
            count = content.lower().count(character.lower())
            res_label.config(text = f'The word/letter "{character}" appears {count} times.', fg = '#fff')  # returns the character with the count
    except:
        # pop up box to show error
        messagebox.showerror("ERROR", "File not found or may not exist.")
    
# creating a function for the search button
def seacrh_btn_function():
    user_input = user_entry.get()              # saving the user's entry in a var
    
    result_text = count_occurrences(user_input, 'sentences.txt') 
    res_label.config(text = result_text) # shows the result

############################## CREATING & DISPLAYING THE REQUIRED WIDGETS ###############################

# creating the heading label
heading_label = Label(root, font = ('Arial', 25, 'bold'), text = "Letter Count", fg = '#fff', bg = 'blue')
heading_label.pack(side = TOP, pady = 10)

# creating the label and entry for the user to enter a character
user_entrylabel = Label(root, font = ('Arial', 12), text = "Enter a character = ", fg = '#fff', bg = 'blue')
user_entrylabel.pack(pady = 10)

user_entry = Entry(root, font = ('Arial', 12, 'bold'), width = 20)
user_entry.pack(pady = 10)

# creating a submit button
submit = Button(root, font = ('Arial', 12), text = "Search", fg = '#fff', bg = 'black', width = 10, command = seacrh_btn_function)
submit.pack(pady = 10)

# creating a result label
res_label = Label(root, text = "", bg = 'blue', font = ('Arial', 12))
res_label.pack(pady = 10)

# running the main window
root.mainloop()

# end of the program