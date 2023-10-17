# creating lines

# importing the tkinter library

import tkinter as tk

window = tk.Tk()

canvas = tk.Canvas(window, width = 800, height = 600)

line1 = canvas.create_line(50, 70, 100, 70, fill = "red", width = 2)

line2 = canvas.create_line(120, 200, 300, 200, fill = "blue", width = 6)

line3dot = canvas.create_line(100, 100, 100, 350, fill = "green", width = 2, dash = (5, 5))

canvas.pack()
window.mainloop()

