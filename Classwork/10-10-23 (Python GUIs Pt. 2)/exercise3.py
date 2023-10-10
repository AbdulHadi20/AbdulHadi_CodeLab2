# calling the tkinter module

from tkinter import *



# creating the function to copy the text entered in the entry widget
def copytext():
    print(user_text.get())

# initializing the window
window = Tk()

# adding the title, size and resolution of the window
window.title("Entry Widget")
window.geometry("500x500")

# creating the entry widget for the user to write text
user_text = StringVar()
text = Entry(window, textvariable = user_text)

# creating the button
myBtn = Button(window, text = "Copy Text", command = copytext)

# creating the label
mylabel = Label(window, text ="Text is displayed")

#packing the entry, button & widget
mylabel.pack(side=BOTTOM)
myBtn.pack(side=BOTTOM)
text.pack(side=BOTTOM)


# running the window
window.mainloop()