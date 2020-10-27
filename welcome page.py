import tkinter
from tkinter import *
from PIL import ImageTk,Image
import os


win = Tk()
win.geometry("1366x720")
image = Image.open('wel.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(win, image = photo_image)
label.pack()
win.title("Welcome Screen")

def click():
    os.system('python imagebtn.py')


button = Button(win, text="Continue to choose plan", bg="grey", fg="white", command=click).place(x=230, y=545)
win.mainloop()
