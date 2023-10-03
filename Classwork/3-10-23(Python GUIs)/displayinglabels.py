# calling the module tkinter

from tkinter import *

label_1 = Tk()
label_1.title("Displaying Labels and Buttons")
label_1.geometry('350x600')


#creating the label widget
myLabel = Label(label_1, text = "I am a label widget.")
myLabel.pack(side = LEFT) 

#creating a button
myButton = Button(label_1, text = "Button")
myButton.pack()


# getting the window ready
label_1.mainloop()