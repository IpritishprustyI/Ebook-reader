import tkinter
from tkinter import *
from tkinter import messagebox

import sys
import os


def base():
    os.system('python loginbasic.py')
def pre():
    os.system('python loginpre.py')
root = tkinter.Tk()
root.geometry("1366x460")

photo = PhotoImage(file="bas.png",)
photo2 = PhotoImage(file="pr.png")
btn = Button(
    root,
    image=photo,
    command=base,
    border=0,
)
btn.pack(side = LEFT, expand = True, fill = X)

btn2 = Button(
    root,
    image=photo2,
    command=pre,
    border=0,
)
btn2.pack(side = TOP, expand = True, fill =X)
root.mainloop()