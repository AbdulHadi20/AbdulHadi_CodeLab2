# importing the tkinter library

import tkinter as tk

app = tk.Tk()

canvas = tk.Canvas(app, width = 800, height = 600)

rect1 = canvas.create_rectangle(10, 10, 150, 100, fill = "blue", outline = "black", width = 2)

rect2 = canvas.create_rectangle(200, 50, 300, 200, fill = "red", outline = "black", width = 2)

rect3 = canvas.create_rectangle(350, 150, 400, 200, fill = "green", outline = "black", width = 2, dash = (5, 5))

canvas.pack()
app.mainloop()