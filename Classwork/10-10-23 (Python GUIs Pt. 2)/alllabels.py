# calling the tkinter module
from tkinter import *

# initializing the root window
app = Tk()

# modifying the window, title, resolution, resizing etc.
app.title("ALL THE WIDGETS")
app.geometry("1366x768")
app.resizable(0, 0)

# creating the label
myLabel = Label(app, text = "Respected Human, Please write something here:")
myLabel.pack(side = TOP, fill = X)

#creating the entry widget
myText = StringVar()
user_text = Entry(app, textvariable = myText)
user_text.pack(side = TOP)

# creating the button
myBtn = Button(app, text = "Press Me !")
myBtn.pack(side = TOP, fill = Y)

# creating the checkbutton
checkBtn = Checkbutton(app, text = "Please tick the box")
checkBtn.pack(side = TOP)

# creating the radio buttons
radio = Radiobutton(app, text = "Human")
radio2 = Radiobutton(app, text = "Alien")
radio.pack(side = TOP)
radio2.pack(side = TOP)

# creating the option menu
optnmenu = OptionMenu(app, "Select Country", "USA", "China", "Russia", "Paksitan")
optnmenu.pack(side = TOP)

#running the window
app.mainloop()

