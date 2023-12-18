"""
Chapter 5 : Exercise 6 : Aritmemetic Operation

Develop a GUI to perform Arithmetic Operations.

- Create a class ArithmeticOperations with the following
- a result variable to store the result after calculation
- a function Calculate() - To perform an arithmetic operation selected by the user.
- You can use Combobox to provide users with options to perform selected arithmetic operations and entry widgets for the values.

"""

# start of the program

# calling the required modules/libraries
from tkinter import *
from tkinter import messagebox

# initializing the root window
root = Tk()

# setting the title, dimensions etc. 
root.title("Arithmetic Operations")
root.geometry("400x400")
root.resizable(0, 0)
root.configure(background = 'red')

############################### CREATING THE REQUIRED CLASS FOR ARITHMETIC OPERATIONS ##########################################

# creating the class named as arithmetic opertaions
class arithmetic_operation:

    # creating a function that performs the operations 
    def calculate(arithmetic_op, num1, num2):

        # using try/except method to handle error outputs efficiently
        try:
            # conditional statements based on the user's choices
            if arithmetic_op == "Addition":
                return num1 + num2
            
            elif arithmetic_op == "Subtraction":
                return num1 - num2
            
            elif arithmetic_op == "Multiplication":
                return num1 * num2
            
            elif arithmetic_op == "Division":
                return num1 / num2 if num2 != 0 else messagebox.showerror("Error", "Cannot divide by zero. Operation Failed") # checks if user entered zero
            
            elif arithmetic_op == "Exponentiation":
                return num1 ** num2
        
        # runs if the code in the try function does not work
        except ValueError:
            messagebox.showinfo("Error", "Please enter numerical values.") # pops up an error window
            return

# creating a function for the buttton to start performing the calculation
def selected_operation():
    # getting the desired arithmetic operation
    selected_operation = arithmetic_list_var.get()

    # using try/except method to haandle errors better
    try:
        # saving the result in a var,calling the calculate function to calculate based on the user's selected arithmetic operation
        result = arithmetic_operation.calculate(selected_operation, float(num1_entry.get()), float(num2_entry.get()))
        
        if result:
            messagebox.showinfo("Result", f"The {selected_operation} of the two numbers is = {result}")
    
    except ValueError:
        messagebox.showinfo("Error", "Please enter valid numeric values.")

################################### CREATING & DISPLAYING THE REQUIRED WIDGETS #############################################
        
# creating a heading label
heading_label = Label(root, font = ('Arial', 25, 'bold'), text = "Arithmetic Operations", bg = 'red', fg = 'white')
heading_label.pack(pady = 10, side = TOP)

# creating a frame to display the widgets in a proper way
framedisplay = Frame(root, bg = 'red')
framedisplay.pack(fill = BOTH, expand = YES)

# creating a lable to inform the user to select an option from the dropdown menu
operation_label = Label(root, font = ('Arial', 12), text = "Please Select an option from the dropdown menu",  bg = "red", fg = 'white')
operation_label.pack(pady = 10, side = TOP)

# creating a dropdown menu that consists of arithmetic operations for the user to select from
arithmetic_list = ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]
arithmetic_list_var = StringVar()
arithmetic_list_var.set(arithmetic_list[0])
operation_option = OptionMenu(root, arithmetic_list_var, *arithmetic_list)
operation_option.pack(pady = 10)

# creating labels and entry widgets for the values
num1_label = Label(framedisplay, font = ('Arial', 12), text = "Enter the first value = ", bg = "red", fg = 'white')
num1_label.grid(row = 0, column = 0, pady = 10, padx = 5)

num1_entry = Entry(framedisplay, font = ('Arial', 12), width = 20)
num1_entry.grid(row = 0, column = 1, padx = 5, pady = 10)

num2_label = Label(framedisplay, font = ('Arial', 12), text = "Enter the second value = ", bg = "red", fg = 'white')
num2_label.grid(row = 1, column = 0, pady = 10, padx = 5)

num2_entry = Entry(framedisplay, font=("Helvetica", 12))
num2_entry.grid(row = 1, column = 1, padx = 5, pady = 10)

# creating a button to perform the calulcations when clicked 
calculate_button = Button(root, font = ("Helvetica", 12,'bold'), text = "Calculate", bg = "green", fg = "white", command = selected_operation)
calculate_button.pack(pady=10)

# runs the program window
root.mainloop()

# end of the program