from cgitb import text
from pickle import OBJ
from sqlite3 import Cursor
from tkinter import*
from tkinter import font
from typing_extensions import Self
from webbrowser import get
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
from random import randint
import pymysql
import getpass

x = randint(1,10)
y = randint(1,10)

z = x + y
while True:
   captcha_ans = input(f"What is {x} + {y} ? ")
   captcha_ans = int(captcha_ans)

   if captcha_ans == z:
       print("You may now access our program")
       break
   else:
       print("Try Again")

class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="black")

        self.bbg = ImageTk.PhotoImage(file="images/Background.jpg")
        bbg = Label(self.root, image=self.bbg).place(x=250, y=0, relwidth=1, relheight=1)

        self.left = ImageTk.PhotoImage(file="images/Left.jpg")
        left = Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

        paragraph = Label(left, text="Already a member?" , font=("time new roman" ,15,"bold"),bg="black",fg="white").place(x=180,y=300)
        paragraph = Label(left, text="Sign in below!" , font=("time new roman" ,15,"bold"),bg="black",fg="white").place(x=180,y=340)

        frame1 = Frame(self.root, bg ="white")
        frame1.place(x=480 , y=100 , width=700 , height=500)

        title = Label(frame1, text="Register" , font=("time new roman" ,22,"bold"), bg="black" ,fg="white").place(x=250,y=30)

        email = Label(frame1, text="Email" , font=("time new roman" ,15,"bold"), bg="white" ,fg="black").place(x=200,y=100)
        self.txt_email = Entry(frame1 , font=("time new roman" ,15),bg = "lightgray")
        self.txt_email.place(x=200, y=140, width=250)

        password = Label(frame1, text="Password" , font=("time new roman" ,15,"bold"), bg="white" ,fg="black").place(x=200,y=180)
        self.txt_password = Entry(frame1 , show="*", font=("time new roman" ,15),bg = "lightgray")
        self.txt_password.place(x=200, y=210, width=250)

        conpass = Label(frame1, text="Confirm Password" , font=("time new roman" ,15,"bold"), bg="white" ,fg="black").place(x=200,y=260)
        self.txt_conpass = Entry(frame1 ,show="*", font=("time new roman" ,15),bg = "lightgray")
        self.txt_conpass.place(x=200, y=300, width=250)

        self.reg = Button(frame1, bd="5", text="Register", font=("time new roman" ,20),command=self.register_d, cursor="hand2", bg="black", fg="white").place(x=280, y=430)

        btn_login = Button(self.root, bd="7", text="Sign In", font=("time new roman", 20), bg="white",fg="black").place(x=180, y=480)

    def register_d(self):

        if self.txt_email.get() == "" or self.txt_password.get() == "" or self.txt_conpass.get() == "":
           messagebox.showerror("warning","Please fill all fields",parent=self.root)

        elif self.txt_password.get() != self.txt_conpass.get():
           messagebox.showerror("warning","Passwords Do Not Match",parent=self.root)

        else: 
            try:
                con = pymysql.connect(host="localhost", user="root", password="", db="login_injector")
                cur = con.cursor()
                cur.execute("insert into login_table1(email,password)values(%s,%s)",
                (

                    self.txt_email.get(),
                    self.txt_password.get()
                    
                ))
                con.commit()
                con.close()
                messagebox.showinfo("success","Registered successfully you may now login",parent=self.root)
            except Exception as es:
             messagebox.showerror("error","error handle, {str(es)}",parent=self.root)





root = Tk()
obj= Register(root)
root.mainloop()