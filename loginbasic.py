import mysql.connector as sql
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk,Image
import os

win = Tk()

win.geometry("500x500")
image = Image.open('bglb.png')
photo_image = ImageTk.PhotoImage(image)
label = Label(win, image = photo_image)
label.pack()
win.title("Login Page Basic")


def login():
    db = sql.connect(host="localhost", user="root", passwd="Prisel@123")

    cur = db.cursor()

    try:

        cur.execute("create database loginbase")

        db = sql.connect(host="localhost", user="root", passwd="Prisel@123", database="loginbase")

        cur = db.cursor()


    except sql.errors.DatabaseError:

        db = sql.connect(host="localhost", user="root", passwd="Prisel@123", database="loginbase")

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

        cur.execute("select * from main where username = '%s' and password = %s" % (user, passwd))

        rud = cur.fetchall()

        if rud:

            messagebox.showinfo("Status", "Welcome back")
            os.system('python gui.py')

            break


        else:

            messagebox.showinfo("Status", "No account found, Please create an account")

            break

    cur.close()

    db.close()


def ok():
    os.system('python Signupbasic.py')


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
button = Button(win, text="Sign up", bg="grey", fg="white", command=ok).place(x=230, y=385)

win.mainloop()
