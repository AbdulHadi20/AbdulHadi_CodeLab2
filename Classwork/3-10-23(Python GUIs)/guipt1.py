# creating a simple GUI (can't be resized)

#importing the module
from tkinter import * 

# creating a window
window = Tk()

# sets the title of the window
window.title('Widgets Example')

# setting the resolution of the window
window.geometry('350x600')

# makes the window static, cannot be resized
window.resizable(0, 0)

# getting the window ready
window.mainloop()