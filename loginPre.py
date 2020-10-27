import mysql.connector as sql
from tkinter import messagebox
from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image

import os

win = Tk()
Myfont=font.Font(family="Helvetica", size=16)

win.geometry("500x500")
image = Image.open('bgl.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(win, image = photo_image)
label.pack()
win.title("Login Page Premium")


def login():
    db = sql.connect(host="localhost", user="root", passwd="Prisel@123")

    cur = db.cursor()

    try:

        cur.execute("create database loginpre")

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

            cur.execute("create table main(username varchar(50) NOT NULL, "  "password int NOT NULL)")


        except sql.errors.ProgrammingError:

            pass

    while True:

        user = user1.get()

        passwd = passwd1.get()

        cur.execute("select * from main where username = '%s' and password = %s" % (user, passwd))

        rud = cur.fetchall()

        if rud:

            messagebox.showinfo("Status", "Welcome back")
            os.system('python bookspre.py')

            break


        else:

            messagebox.showinfo("Status", "No account found, Please create an account")

            break

    cur.close()

    db.close()


def ok():
    os.system( 'python signpre.py')


userlvl = Label(win, text="Username :")

passwdlvl = Label(win, text=" 4 digit PIN  :")

user1 = Entry(win, textvariable=StringVar())

passwd1 = Entry(win, textvariable=IntVar().set(""))

enter = Button(win, text="Enter", command=lambda: login(), bd=0)

enter.configure(bg="pink")

user1.place(x=200, y=220)

passwd1.place(x=200, y=270)

userlvl.place(x=130, y=220)

passwdlvl.place(x=130, y=270)

enter.place(x=238, y=325)
button = Button(win, text="Sign UP", bg="grey", fg="white", command=ok).place(x=230, y=385)

win.mainloop()
