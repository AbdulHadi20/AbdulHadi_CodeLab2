# managing layouts

# calling the tkinter library & importiing the random module
from tkinter import * 
import random

# initializing the root window
app = Tk()

# adding title of the window
app.title("Managing Layouts")

# creating the labels
lbl_1 = Label(app, text = "A",  bg = 'red', relief = GROOVE, width = 12, bd = 5)
lbl_2 = Label(app, text = "B", bg = 'yellow', width = 12)
lbl_3 = Label(app, text = "C", bg = 'blue', width = 12)
lbl_4 = Label(app, text = "D", bg = 'white', width = 12)

# packing the labels
lbl_1.pack(side = 'top', fill = X, expand = 1)
lbl_2.pack(side = 'bottom')
lbl_3.pack(side = 'left', fill = X, expand = 1)
lbl_4.pack(side = 'right')

# running the window
app.mainloop()
