# calling the library
from tkinter import *


#creating a function for clicking the button
#once the button is clicked, the button changes into a label
def onclick():
    print("Changed Text")

    #creating a a label
    theLabel = Label(window, text = "Changed Text")
    theLabel.pack(side = BOTTOM)


#initializing the root window
window = Tk()

#setting the window title, size dimensions etc.
window.title("Label Widget")
window.geometry("800x600")

#creating a button
theBtn = Button(window, text = "Changed Text", command = onclick)
theBtn.place(x = 353, y = 550)

#getting the window ready
window.mainloop()