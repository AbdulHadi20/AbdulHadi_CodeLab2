"""
Chapter 2 : Exercise I : Count Characters

Writing a program that asks the user to enter a string, then counts out the vowels and consonants, and special characters

"""

# start of the program

# importing the tkinter module
from tkinter import *

# creating the root window
root =Tk()

# setting the dimensions, title, etc
root.title("Count Characters")                  # sets the title 
root.geometry("600x400")                        # sets the width and height (geometry)
root.resizable(0, 0)                            # sets the window to disallow resizing
root.configure(background = 'grey')             # sets the background color

###################### CREATING REQUIRED FUNCTIONS ###################################################

# creating a function to count the characters  
def count_characters():
    user_entry = str(textbox_str.get())                  # saving the user's entry 
 
    vowels = 'aeiou'                                     # storing the vowels in a variable
    alpha_in_sentence  = 0                               # storing the number of alphabets
    letters_in_sentence = 0                              # storing the number of letters
    vowels_in_sentence = 0                               # storing the number of vowels
    consonants_in_sentence = 0                           # storing the number of consonants
    spec_char_in_sentence = 0                            # storing the number of special characters
    digits_in_sentence = 0                               # storing the number of digits

    for char in user_entry:                              # creating a for loop to go through the sentence
        letters_in_sentence += 1                         # adds a letter every time 

        if char.isalpha():                               # runs if character is an alphabet
            alpha_in_sentence += 1

            if char.lower() in vowels:                   # a nested loop, runs if the character is a vowel
                vowels_in_sentence += 1 
 
            else:                                        # runs if the alphabet is a consonaant
                consonants_in_sentence += 1

        elif char.isdigit():                             # runs if the letter(character) is a digit 
            digits_in_sentence += 1

        else:                                            # runs if it is a special character
            spec_char_in_sentence += 1

        # displaying the result   
        result_str.set(f"Letters: {letters_in_sentence} \n Alphabets: {alpha_in_sentence} \n Vowels: {vowels_in_sentence} \n Consonants: {consonants_in_sentence} \n Digits: {digits_in_sentence} \n Special Characters: {spec_char_in_sentence}")

# creating a function to clear out the text box
def clear():
    textbox.delete(0, "end")


###################### CREATING REQUIRED WIDGETS ####################################################

# creating a heading label
heading_label = Label(root, font = ('Arial', 20, 'bold'), text = "Count Characters", bg = 'grey')

# creating a frame for the label and entry widgets
frame = LabelFrame(root, border = 0, bg = 'grey') 

# creating a label for the user's instruction
label = Label(frame, font = ('Arial', 14), text = "Please type in a sentence = ", bg = 'grey')

# creating an entry widget for the user's typing
textbox_str = StringVar()
textbox = Entry(frame, font = ('Arial', 14), width = 20, textvariable = textbox_str)

# creating a button to start counting the characters
button = Button(frame, font = ('Arial', 16, 'bold'), text = "Count Characters", bg = 'brown', fg = 'white', padx = 5, pady = 5, command = count_characters)

# creating a clear button 
clearbtn = Button(frame, font = ('Arial', 16, 'bold'), text = "Clear", bg = 'brown', fg = 'white', padx = 5, pady = 5, command = clear)

# creating a label for the result to display
result_str = StringVar()
result = Label(root, textvariable = result_str,  bg = 'grey', font = ('Arial', 14))

###################### DISPLAYING THE REQURIED WIDGETS ##############################################

heading_label.pack(side = TOP, anchor = N, padx = 3, pady = 7)             # displays the heading
frame.pack(side = TOP, anchor = N, padx = 3, pady = 7)                     # displays the frame
label.grid(row = 0, column = 0, padx = 5, pady = 5)                        # displays the label message
textbox.grid(row = 0, column = 1, padx = 5, pady = 5)                      # displays the entry widget to write
button.grid(row = 1, column = 1, padx = 5, pady = 5)                       # displays the count button
clearbtn.grid(row = 1, column = 0, padx = 5, pady = 5)                     # displays the clear button
result.pack(side = BOTTOM, anchor = S, padx = 5, pady = 7 )                # displays the result


# running the root window (mainloop)
root.mainloop()

# end of the program