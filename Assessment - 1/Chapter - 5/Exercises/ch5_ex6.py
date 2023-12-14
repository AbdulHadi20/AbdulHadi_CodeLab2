"""
Chapter 5 : Exercise 6 : Aritmemetic Operation

Develop a GUI to perform Arithmetic Operations.

- Create a class ArithmeticOperations with the following
- a result variable to store the result after calculation
- a function Calculate() - To perform an arithmetic operation selected by the user.
- You can use Combobox to provide users with options to perform selected arithmetic operations and entry widgets for the values.

"""

# start of the program

# Importing modules from the tkinter library
from tkinter import *
from tkinter import messagebox

# initializing the root window
root = Tk()

# setting the title, dimensions etc. 
root.title("Arithmetic Operations")
root.geometry()

# Class for performing arithmetic operations
class ArithmeticOperations:
    def calculate(operation, value1, value2):
        try:
            # To Perform the selected arithmetic operation
            if operation == "Addition":
                return value1 + value2
            elif operation == "Subtraction":
                return value1 - value2
            elif operation == "Multiplication":
                return value1 * value2
            elif operation == "Division":
                # Check for division by zero
                return value1 / value2 if value2 != 0 else messagebox.showerror("Error", "Cannot divide by zero.")
            elif operation == "Exponentiation":
                return value1 ** value2
        except ValueError:
            # Handle invalid input values
            messagebox.showinfo("Error", "Please enter valid numeric values.")
            return

# Function to perform calculation when the "Calculate" button is clicked
def perform_calculation():
    # Getting the selected arithmetic operation
    selected_operation = operation_var.get()

    try:
        # Getting values from entry widgets
        result = ArithmeticOperations.calculate(selected_operation, float(value1_entry.get()), float(value2_entry.get()))
        if result:
            # Displaying the result in a messagebox pop-up
            messagebox.showinfo("Result", f"The result is: {result}")
    except ValueError:
        # Handle invalid input values
        messagebox.showinfo("Error", "Please enter valid numeric values.")

# Widgets for Arithmetic Operations tab
arithmetic_tab = Frame(root, bg="#22263d", pady=20)

# Label for selecting the arithmetic operation
operation_label = Label(arithmetic_tab, text='Select Operation:', 
                        font=('Roboto', 12, 'bold'),bg="#22263d",fg='white')
operation_label.pack()

# Options for the arithmetic operations presented in a drop-down menu
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Exponentiation"]
operation_var = StringVar()
operation_var.set(operations[0])
operation_option = OptionMenu(arithmetic_tab, operation_var, *operations)
operation_option.pack(pady=10)

# Labels and Entry widgets for inputting numeric values
value1_label = Label(arithmetic_tab, text="Enter Value 1:", 
                     font=('Roboto', 12, 'bold'),bg="#22263d",fg='white')
value1_label.pack(pady=5)
value1_entry = Entry(arithmetic_tab, font=("Helvetica", 12))
value1_entry.pack(pady=5)

value2_label = Label(arithmetic_tab, text="Enter Value 2:", 
                     font=('Roboto', 12, 'bold'),bg="#22263d",fg='white')
value2_label.pack(pady=5)
value2_entry = Entry(arithmetic_tab, font=("Helvetica", 12))
value2_entry.pack(pady=5)

# Button to trigger the calculation with specified text, command, font, and color
calculate_button = Button(arithmetic_tab, text='Calculate', 
                command=perform_calculation, font=("Helvetica", 12,'bold'), bg="#4CAF50", fg="white")
calculate_button.pack(pady=10)

# Packing the Arithmetic Operations tab
arithmetic_tab.pack(fill=BOTH, expand=YES)

# Run the main event loop
root.mainloop()

# End Marker
