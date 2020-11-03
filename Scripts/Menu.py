from tkinter import *

root = Tk()

menubar = Menu(root)
root.config(menu=menubar)

filemenu = Menu(menubar)
filemenu.add_command (label="Nuevo")
filemenu.add_command (label="Nuevo")
filemenu.add_command (label="Nuevo")
filemenu.add_command (label="Nuevo")


menubar.add_cascade (label="Archivo", menu=filemenu)


root.mainloop()