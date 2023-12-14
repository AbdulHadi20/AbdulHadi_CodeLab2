""" 
Chapter 5 : Exercise 3 : Employee Class

Develop a GUI using Tkinter to Create an employee class with the following members: name, age, id, salary

Add the following methods: setData() - should allow employee data to be set via user input,getData()- should output employee data to the console
Create a list of 5 employees. Ask the user to enter the details of 5 employees using the add_employee method and then display the output using 
the display_emloyee method as mentioned below Expected output:

Name	           Position	            Salary	        ID
Alice	           Manager		        9500.0	        1
Bob	               Accountant	        6000.0	        2
Brain	           Social Media	        4000.0	        3
Frank	           Salesman         	2500.0	        4
Marker	           Clerk	        	1500.0	        5

"""

# start of the program

# importing the required modules/libraries
import tkinter as tk

# creating a class for employees
class Employee:
    # a function to initialize the vars
    def __init__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = ""

    # a function to save the user input in a var
    def setData(self, name, position, salary, emp_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = emp_id

    # a function to return data
    def getData(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.id}"


# creating a class for the GUI interface
class EmployeeGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Class")
        self.geometry("400x600")
        self.resizable(0, 0)
        self.configure(background = 'cyan')
        self.employees_added = 0
        self.create_employee_data_fields()

        #  creating a button to add employees
        add_button = tk.Button(self, text = "Add Employee", command = self.add_employee, font = ('Arial', 18, 'bold'), bg = 'purple', fg = '#fff')
        add_button.pack(pady = 10)

        #  creating a button to clear data fields for employees
        add_button = tk.Button(self, text = "Clear", command = self.clear_entries, font = ('Arial', 18, 'bold'), bg = 'purple', fg = '#fff')
        add_button.pack(pady = 10)

    # creating the data fields for the users to enter employee data
    def create_employee_data_fields(self):

        self.heading_label = tk.Label(self, text = "EMPLOYEE CLASS DATA ENTRY", font = ('Arial', 18, 'bold'), bg = 'cyan')
        self.heading_label.pack(pady = 10)
        self.name_label = tk.Label(self, text="Name", font = ('Arial', 14), bg = 'cyan')
        self.name_label.pack(pady = 10)
        self.name_entry = tk.Entry(self,font = ('Arial', 14))
        self.name_entry.pack(pady = 10)

        self.position_label = tk.Label(self, text = "Position", font = ('Arial', 14), bg = 'cyan')
        self.position_label.pack(pady = 10)
        self.position_entry = tk.Entry(self, font = ('Arial', 14))
        self.position_entry.pack(pady = 10)

        self.salary_label = tk.Label(self, text = "Salary", font = ('Arial', 14), bg = 'cyan')
        self.salary_label.pack(pady = 10)
        self.salary_entry = tk.Entry(self, font = ('Arial', 14))
        self.salary_entry.pack(pady = 10)

        self.id_label = tk.Label(self, text = "ID", font = ('Arial', 14), bg = 'cyan')
        self.id_label.pack(pady = 10)
        self.id_entry = tk.Entry(self, font = ('Arial', 14))
        self.id_entry.pack(pady = 10)

    # a function to add employees
    def add_employee(self):
        if self.employees_added >= 5:
            print("Maximum number of employees reached (5 employees).")
        else:
            name = self.name_entry.get()
            position = self.position_entry.get()
            salary = float(self.salary_entry.get())
            emp_id = self.id_entry.get()

            employee = Employee()
            employee.setData(name, position, salary, emp_id)
            print("Employee Added:")
            print(employee.getData())

            self.employees_added += 1

    # a function to delete all the entries     
    def clear_entries(self):
        self.name_entry.delete(0, "")
        self.position_entry.delete(0, "")
        self.salary_entry.delete(0, "")
        self.id_entry.delete(0, "")


# running the main windows (mainloop)
app = EmployeeGUI()
app.mainloop()

# end of the program