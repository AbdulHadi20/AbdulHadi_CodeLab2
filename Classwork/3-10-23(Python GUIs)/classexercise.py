# calling the library

from tkinter import *

# creating a function
def onclicks():
    print("Hello, You Clicked a button!!")

# initiating the toolkit
window = Tk()

#setting the title, and size for the window
window.title("Exercise Program 1")
window.geometry('400x400')

#creating a button
myBtn = Button(window, text = "Click Here!", command = onclicks)
myBtn.pack(side = TOP)


#getting the window ready
window.mainloop()
