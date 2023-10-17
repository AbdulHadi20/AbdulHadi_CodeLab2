# importing tkinter library

import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width = 800, height = 600)

oval1 = canvas.create_oval(170, 180, 300, 310, fill = "red", outline = "white", width = 2)

text = canvas.create_text(500, 510, text = "Hello", font = ("Roboto", 14), fill = "green")

canvas.pack()
root.mainloop()