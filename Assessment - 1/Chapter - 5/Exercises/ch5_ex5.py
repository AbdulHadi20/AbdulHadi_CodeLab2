"""
Chapter 5 : Exercise 5 : Playing around in class

Use this exercise to play around with creating and accessing class members and methods. Develop a GUI using Tkinter to Create a class 
called Animal

- Give the class at least the following members Type, Name, Colour, Age, Weight, Noise
- The class should have the following methods sayHello() - says its name via print,makeNoise() -make an appropriate noise via print, 
animalDetails() -output all the details of the animal object
- Instantiate at least two objects from your animal class (e.g. Dog, Cow)
- Set values for each of the variables
- Invoke each of the class functions

"""

# start of the program

# importing te required modules/libraries
from tkinter import *
from tkinter import messagebox

# initializing the root window
app = Tk()

# customizing the app window
app.title("Playing Around in Class")
app.geometry("400x400")
app.resizable(0, 0)
app.configure(background = 'cyan')

################################## CREATING THE REQUIRED CLASS FOR ANIMALS ###########################################

# creating a class called Animal
class Animal:

    # creating a function to get the data stored entered by the user
    def set_data(animal, animal_type, name, colour, age, weight, noise):
        animal.type = animal_type  
        animal.name = name 
        animal.colour = colour
        animal.age = age
        animal.weight = weight
        animal.noise = noise

    def say_hello(animal):
        # to Return a greeting message using the animal's name
        return f"{animal.name} says hello!"

    def make_noise(animal):
        # Return the noise the animal makes along with its name
        return f"{animal.name} makes the noise: {animal.noise}"

    def animal_details(animal):
        # Return all details of the animal
        details = f"Type: {animal.type}\nName: {animal.name}\nColour: {animal.colour}\nAge: {animal.age}\nWeight: {animal.weight}\nNoise: {animal.noise}"
        return details

# making a function to create Animal objects and invoke class functions
def create_animal_objects():
    # Getting values from entry boxes
    animal_type = type_entry.get()
    name = name_entry.get()
    colour = colour_entry.get()
    age = age_entry.get()
    weight = weight_entry.get()
    noise = noise_entry.get()

    # Creating an instance of the Animal class
    animal_object = Animal()

    # Setting data for the Animal instance
    animal_object.set_data(animal_type, name, colour, age, weight, noise)

    # the message to display
    message = f"{animal_object.say_hello()}\n{animal_object.make_noise()}\n{animal_object.animal_details()}"

    # the message in a messagebox
    messagebox.showinfo("Animal Details", message)

# Creating the main window
root = Tk()

# Setting the title for the window
root.title("Animal Class GUI")

# Setting the background color
root.config(bg="#22263d")

# Setting the window size
root.geometry("400x500")

# Labels and Entry Boxes for input
type_label = Label(root, text="Enter Type:",font=('Roboto', 12, 'bold'),bg="#22263d",fg='white') # For Type:
type_label.pack(pady=5)
type_entry = Entry(root, font=("Helvetica", 12))
type_entry.pack(pady=5)

name_label = Label(root, text="Enter Name:",font=('Roboto', 12, 'bold'),bg="#22263d",fg='white') # For  Name:
name_label.pack(pady=5)
name_entry = Entry(root, font=("Helvetica", 12))
name_entry.pack(pady=5)

colour_label = Label(root, text="Enter Colour:",font=('Roboto', 12, 'bold'),bg="#22263d",fg='white') # For Colour:
colour_label.pack(pady=5)
colour_entry = Entry(root, font=("Helvetica", 12))
colour_entry.pack(pady=5)

age_label = Label(root, text="Enter Age:",font=('Roboto', 12, 'bold'),bg="#22263d",fg='white') # For Age:
age_label.pack(pady=5)
age_entry = Entry(root, font=("Helvetica", 12))
age_entry.pack(pady=5)

weight_label = Label(root, text="Enter Weight:",font=('Roboto', 12, 'bold'),bg="#22263d",fg='white') # For Weight:
weight_label.pack(pady=5)
weight_entry = Entry(root, font=("Helvetica", 12))
weight_entry.pack(pady=5)

noise_label = Label(root, text="Enter Noise:",font=('Roboto', 12, 'bold'),bg="#22263d",fg='white') # For Noise:
noise_label.pack(pady=5)
noise_entry = Entry(root, font=("Helvetica", 12))
noise_entry.pack(pady=5)

# Button to create Animal objects and call class functions
create_animal_button = Button(root, text="Create Animal", command=create_animal_objects, bg="#4CAF50", fg="white", font=("Roboto", 12, 'bold'))
create_animal_button.pack(pady=20)

# Run the main event loop
root.mainloop()

# End Marker
