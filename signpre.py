from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import mysql.connector as sql
from PIL import Image, ImageTk
win = Tk()

win.geometry("500x500")
image = Image.open('bg.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(win, image = photo_image)
label.pack()
win.title("Signup Page Premium")
Myfont=font.Font(family="Helvetica", size=16)
Myfont1=font.Font(family="Times", size=19,slant ="italic")
def login():
    db = sql.connect(host="localhost", user="root", passwd="Prisel@123")

    cur = db.cursor()

    try:

        cur.execute("create database login")

        db = sql.connect(host="localhost", user="root", passwd="Prisel@123", database="loginpre")

        cur = db.cursor()


    except sql.errors.DatabaseError:

        db = sql.connect(host="localhost", user="root", passwd="Prisel@123", database="loginpre")

        cur = db.cursor()

        try:

            cur.execute("create table main(username varchar(50), NOT NULL, password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass


    finally:

        try:

            cur.execute("create table main(username varchar(50) NOT NULL, "

                        "password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass

    while True:

        user = user1.get()

        passwd = passwd1.get()

        cur.execute("insert into main values('{}', {})".format(str(user), passwd))

        db.commit()
        messagebox.showinfo("Status", "Account created")
        break


    cur.close()

    db.close()


userlvl = Label(win, text="Username :")

passwdlvl = Label(win, text="Password  :")

user1 = Entry(win, textvariable=StringVar())

passwd1 = Entry(win, textvariable=IntVar().set(""))

enter = Button(win, text="Enter", command=lambda: login(), bd=0)

enter.configure(bg="pink")

user1.place(x=200, y=220)

passwd1.place(x=200, y=270)

userlvl.place(x=130, y=220)

passwdlvl.place(x=130, y=270)

enter.place(x=238, y=325)

win.mainloop()