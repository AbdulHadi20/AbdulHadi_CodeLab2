# importing the library
from tkinter import *

#activating the toolkit
window = Tk()

# giving a title to the window
window.title("Working with pack()")

#creating buttons
Button(window, text = "A").pack(side = LEFT, expand = YES, fill = Y)
Button(window, text = "B").pack(side = TOP, expand = YES, fill = BOTH)
Button(window, text = "C").pack(side = RIGHT, expand = YES, anchor = NE, fill = NONE, pady = 6)
Button(window, text = "D").pack(side = BOTTOM, expand = NO, fill = Y, pady = 6)

#getting the window ready
window.mainloop()

