import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import os
def btnclick():
    messagebox.showinfo("Message","Enjoy your books!")
    os.system('python speach.py') # Ma'am,the same speach file is used to reduce space

root = tkinter.Tk()
root.geometry("1366x720")
root.configure(bg="black")


photo = PhotoImage(file="1.png",)
photo2 = PhotoImage(file="2.png")
photo3 = PhotoImage(file="3.png")
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