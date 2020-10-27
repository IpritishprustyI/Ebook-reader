import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import os

def btnclick():
    messagebox.showinfo("Message","Enjoy your book!")
    os.system('python speach.py')

root = tkinter.Tk()
root.geometry("1366x720")
root.configure(bg="black")


photo = PhotoImage(file="4.png",)
photo2 = PhotoImage(file="5.png")
photo3 = PhotoImage(file="6.png")
btn = Button(
    root,
    compound = CENTER,
    image=photo,
    command=btnclick,
    border=0,
    bg='antique white'

)
btn.pack(side = LEFT, expand = True, fill = BOTH)

btn2 = Button(
    root,
    compound = CENTER,
    image=photo2,
    command=btnclick,
    border=0,
    bg='linen'
)
btn2.pack(side = LEFT, expand = True, fill =BOTH)

btn3 = Button(
    root,
    compound = CENTER,
    image=photo3,
    command=btnclick,
    border=0,
    bg='blanched almond'
)
btn3.pack(side = LEFT, expand = True, fill =BOTH)

root.mainloop()