# importing the tkinter library

import tkinter as tk

app = tk.Tk()

canvas = tk.Canvas(app, width = 800, height = 600)

rect1 = canvas.create_rectangle(70, 80, 100, 110, fill = "yellow")

canvas.pack()
app.mainloop()