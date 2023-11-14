import tkinter as tk

class dog:
    def __init__(self, name , age):
        self.name = name
        self.age = age

    def woof(self):
        return f"{self.name}, says woof!"
    

dog1 = dog("German Shepherd", 10)
dog2 = dog("Husky", 8)

old_dog = dog1 if dog1.age > dog2.age else dog2

class dog_GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dogs are cool")
        self.geometry("400x400")

        self.display_dog_info()

    def display_dog_info(self):
        lbl1 = tk.Label(self, f"Dog1: {dog1.name}, {dog1.age} years old")
        lbl1.pack()

        lbl2 = tk.Label(self, f"Dog2: {dog2.name}, {dog2.age} years old")
        lbl2.pack()

        old_dog_label = tk.Label(self, text = f"The older dog is {old_dog.name}")
        old_dog_label.pack()

        woofbtn = tk.Button(self, text = "make woof")
        woofbtn.pack()

    def woof(self):
        result = old_dog.woof()
        woof_lbl = tk.Label(self, text = result)
        woof_lbl.pack()

app = dog_GUI()
app.mainloop()