"""
Chapter 5 : Exercise 1 : Woof Woof

Develop a GUI using Tkinter with a class that defines the characteristics of a dog. The program should instantiate two objects 
from this class and assign data to its members. The program should then output the data from each object and the oldest dog 
should woof via a class method.

"""

# start of the program

# importing the required modules/libraries
import tkinter as tk

################## CREATING THE CLASS FOR THE GUI WINDOW ############################################

# creating a class named DogGUI
class DogGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Woof Woof")
        self.geometry("400x350")
        self.resizable(0, 0)
        self.configure(background = 'gold')
        self.display_dog_info()

    def display_dog_info(self):

        # creating a heading
        heading = tk.Label(self, text = "WOOF WOOF", font = ('Arial', 20, 'bold'), bg = 'gold')
        heading.pack(side = "top", pady = 10) 

        # creating a label and entry for the dogs
        # label and entry for dog 1
        label_dog1 = tk.Label(self, text = f"Dog 1: {dog1.name}, {dog1.age} years old", font = ('Arial', 14), bg = 'gold')
        label_dog1.pack(pady = 10)

        # label and entry for dog 2
        label_dog2 = tk.Label(self, text = f"Dog 2: {dog2.name}, {dog2.age} years old", font = ('Arial', 14), bg = 'gold')
        label_dog2.pack(pady = 10)

        # label for the oldest dog
        oldest_dog_label = tk.Label(self, text = f"The oldest dog is {oldest_dog.name}", font = ('Arial', 14), bg = 'gold')
        oldest_dog_label.pack(pady = 10)

        # button widget 
        woof_btn = tk.Button(self, text = "Press ME", command = self.woof, font = ('Arial', 20, 'bold'), bg = 'orange')
        woof_btn.pack(pady = 10)

    def woof(self):
        result = oldest_dog.woof()
        woof_label = tk.Label(self, text=result, font = ('Arial', 14), bg = 'gold')
        woof_label.pack()

################################# CREATING A CLASS FOR THE DOGS ################################
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def woof(self):
        return f"{self.name} says woof!"


# Create two dog objects
dog1 = Dog("Pitbull",17)
dog2 = Dog("Golden Retriever", 20)

# Determine the oldest dog
oldest_dog = dog1 if dog1.age > dog2.age else dog2
# Instantiate the DogGUI class
app = DogGUI()
app.mainloop()

# end of program