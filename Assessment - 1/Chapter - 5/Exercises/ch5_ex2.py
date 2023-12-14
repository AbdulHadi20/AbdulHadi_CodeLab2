"""
Chapter 5 : Exercise 2 : Student Class

Develop a GUI using Tkinter to Create a class called Students.

- The class should have the following members.Name (string), Mark1 (int), Mark2 (int), Mark3 (int) 
- The class should have the following methods calcGrade() - should return an average from the three marks.display()- should output 
the student name and calculated grade average
- Create one object using a constructor that contains parameters to initialize all of the variables
- Ask user to input the variable values using input() and pass the values to the second object

"""

# start of the program

# importing the required modules/libraries
from tkinter import *
from tkinter import messagebox

# initializing the root window
window = Tk()

# setting the window titlw, size, etc.
window.title("Student Class GUI")
window.geometry("550x300")
window.resizable(0, 0)
window.configure(background = 'yellow')

###################################### CREATING THE REQUIRED CLASSES & FUNCTIONS ####################################

# creating and defining a class for students
class Student:
    # creating a function to set data for a student
    def getdata(student, name, subject1, subject2, subject3):
        student.name = name
        student.subject1 = subject1
        student.subject1 = subject2
        student.subject1 = subject3

    # creating a function that calculates the average grade of a student
    def gradecal(student):
        # getting the average of three subjects
        return (student.subject1 + student.subject1 + student.subject1) / 3

    # function that will display the student information
    def display(student):
        # returns the output with the student name and average grade
        return f"Student Name: {student.name}\nAverage Grade: {student.gradecal():}"

# function that creates the student object
def create_student_object():
    # getting user values
    name = name_entry.get()
    subject1 = float(subject1_entry.get())
    subject2 = float(subject2_entry.get())
    subject3 = float(subject3_entry.get())
    
    # student object with the provided values
    student_object = Student()
    student_object.getdata(name, subject1, subject2, subject3 )
    
    # student information displayed in a messagebox
    messagebox.showinfo("Student Information", student_object.display())

############################### CREATING THE REQUIRED WIDGETS AND DISPLAYING THEM ################################################

# creating the labels and entry widgets for the name and subjects

# label for the name
name_label = Label(window, text = "Enter your name = ", bg = 'yellow') 
name_label.grid(row = 0, column = 0, pady = 10, padx = 20)

# entry for the name
name_entry = Entry(window, font=("Roboto", 14)) 
name_entry.grid(row = 0, column = 1, pady = 10, padx = 20)

# label for subject 1
subject1_label = Label(window, text = "Enter Marks for Subject 1 = ", bg = 'yellow') 
subject1_label.grid(row = 1, column = 0, pady = 10, padx = 20)

# entry for subject 1
subject1_entry = Entry(window, font = ("Roboto", 14))
subject1_entry.grid(row = 1, column = 1, pady = 10, padx = 20)

# label for subject 2
subject2_label = Label(window, text = "Enter Marks for Subject 2 = ", bg = 'yellow') 
subject2_label.grid(row = 2, column = 0, pady = 10, padx = 20)

# entry for subject 2
subject2_entry = Entry(window, font = ("Roboto", 14))
subject2_entry.grid(row = 2, column = 1, pady = 10, padx = 20)

# label for subject 3
subject3_label = Label(window, text = "Enter Marks for Subject 3 = ", bg = 'yellow') 
subject3_label.grid(row = 3, column = 0, pady = 10, padx = 20)

# entry for subject 3
subject3_entry = Entry(window, font = ("Roboto", 14))
subject3_entry.grid(row = 3, column = 1, pady = 10, padx = 20)

# button to create a student object
create_student_button = Button(window, text = "Create Student", command = create_student_object, bg = "green", fg = "white", font =("Roboto", 12, 'bold'))
create_student_button.grid(row = 4, column = 0, pady = 10, columnspan = 30)

# Run the main event loop
window.mainloop()

# end of the program