# creating canvas

#importing the tkinter library

import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width = 800, height = 600)

line = canvas.create_line(3, 3, 100, 323, width = 2)

canvas.pack()
root.mainloop()