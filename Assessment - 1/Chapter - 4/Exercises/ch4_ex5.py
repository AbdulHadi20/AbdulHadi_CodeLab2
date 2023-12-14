"""
Chapter 4 : Exercise 5 : Password Check

Develop a GUI App to check the validity of a password given by the user in the entry widget. The password should satisfy the 
following criteria:

- Contain at least 1 letter between a and z
- Contain at least 1 number between 0 and 9
- Contain at least 1 letter between A and Z
- Contain at least 1 character from $, #, @
- Minimum length of password: 6
- Maximum length of password: 12

Ask user to include a maximum of 5 passcode attempts. Each time the user enters an incorrect passcode, they should be prompted 
of how many passcode attempts remain. If there are 5 failed passcode attempts the while loop should break and inform the user 
that the authorities have been alerted!    

"""

# start of the program


# importing the required modules/libraries
from tkinter import *
from tkinter import messagebox

# initializing the root window
window = Tk()

# setting the title, dimensions, bg color, etc. 
window.title("Password Checker")                # sets the title
window.geometry("800x700")                      # sets the dimensions
window.resizable(0, 0)                          # disables the resizing
window.configure(background = 'yellow')

##################################### CREATING THE REQUIRED FUNCTIONS #########################################

# storing the number of attempts in a var
attempts_var = StringVar()
attempts_var.set("5")

# creating the function to check if the password is valid
def pass_checker(passkey):
    
    # putting up a condition to check the length of the password is of the correct length
    if not (6 <= len(passkey) <= 12):

        return False, "Password length must be between 6 and 12 characters.\n"
    

    # checking if the password has lowercase, numbers, uppercase, and special characters
    lower = any(char.islower() for char in passkey)                 # checks for lowercase
    num = any(char.isdigit() for char in passkey)                   # checks for numbers
    upper = any(char.isupper() for char in passkey)                 # checks for uppercase
    special_char = any(char in "$#@ " for char in passkey)          # checks for special characters


    if lower and num and upper and special_char:  # this runs if all the required criteria is true
        result_label.config(text = "Valid Password")
        window.configure(background = 'green')  
    else:             # runs if the criteria is not met
        result_label.config(text = "Invalid Password \n Your password must include: \n - an upper & lowwercase char \n - a number & symbol")
        window.configure(background = 'orange')


# creating a function for the button
def submit_passkey():
    
    # storing the user's entry in a var
    password_key = passkey_entry.get()
    available_att = int(attempts_var.get())

    if available_att > 0:          # runs if attempts left are more than 0
        is_valid, message = pass_checker(password_key)

        if is_valid:                          # runs if password is valid and turns window to green
            result_label.config(text="Password is valid.")
            window.configure(background = 'green')

        else:                                # runs if the criteria isnt met, and reduces the attempts left
            available_att -= 1
            result_text = f"{message} "
 
            if available_att == 0:          # nested conditional statement, runs if attempts are all used, pops out an error window
                window.configure(background = 'red')
                messagebox.showerror("WARNING",'The authorities have been alerted of your suspicious activity')

                submit_btn.config(state = DISABLED)  # disables the submit button

            result_label.config(text=result_text)        # displayig the results 
            attempts_var.set(str(available_att))
    else:
        window.configure(background = 'red')
        messagebox.showerror("WARNING",'The authorities have been alerted of your suspicious activity')

##################################### CREATING THE REQUIRED WIDGETS & DISPLAYING THEM #########################################

# creating a heading label and packing it
heading_label = Label(window, font = ('Roboto', 20, 'bold'), bg = 'yellow', text = "Password Checker")
heading_label.grid(row = 0, column = 0, columnspan = 50,pady = 10, padx = 20)

# creating a label and entry widget for the password
passkey_label = Label(window, text="Enter Password = ", font = ('Roboto', 20, 'bold'), bg = 'yellow')
passkey_label.grid(row = 1, column = 0, pady = 15)

passkey_entry = Entry(window, font = ('Roboto', 20, 'bold'), show="*")
passkey_entry.grid(row = 1, column = 1, pady = 15)

# creating a button for submitting password
submit_btn = Button(window, text="Check Password", font = ('Roboto', 20, 'bold'), bg = 'skyblue', command=submit_passkey)
submit_btn.grid(row = 2, column = 0, columnspan = 50,pady = 10)

# creating a label to display the result and attempts left
result_label = Label(window, text="", font = ('Roboto', 20, 'bold'), bg = 'yellow')
result_label.grid(row = 3, column = 0, columnspan = 50,pady = 10)

# creating a label that displays the attempts left
attempts_label = Label(window, text="Attempts left = ", font = ('Roboto', 20, 'bold'), bg = 'yellow')
attempts_label.grid(row = 4, column = 0, columnspan = 50,pady = 10)

attempts_display = Label(window, textvariable = attempts_var, font = ('Roboto', 20, 'bold'), bg = 'yellow')
attempts_display.grid()

# wunning the main window
window.mainloop()

# end of the program
