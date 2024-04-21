from tkinter import *

root = Tk()

frame = Frame(root, width=500, height=400)
frame.pack()

label = Label(frame, text="Hola desde Python")
label.place(x=100, y=20)

root.mainloop()