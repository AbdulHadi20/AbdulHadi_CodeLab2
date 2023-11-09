#ch5ex3

import tkinter as tk

# calling thr class

class Employee:
    def __init__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.id = 0
        self.age = ""

    def setData(self, name, position, salary, id, age):
        self.name = name
        self.position = position
        self.salary = salary
        self.id = id
        self.age = age

    def getData(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, ID: {self.id}, Age: {self.age}"
    

class Employee_GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employee Details")
        self.geometry("700x700")
        self.employees = []
        self.add_employee()

    def add_employee(self):
        for _ in range(5):
            name = input("\n Enter the name = ")
            position = input("\n Enter the position = ")
            salary = input("\n Enter the salary = ")
            id = input("\n Enter the ID = ")
            age = input("\n Enter the age = ")

            employee = Employee()
            employee.setData(name, position, salary, id, age)

            self.employees.append(employee)

        self.display_employees()

    def display_employees(self):
        for employee in self.employees:
            print(employee.getData())

app = Employee_GUI()
app.mainloop()