from tkinter import*
from tkinter import ttk, messagebox
from PIL import Image, ImageTk,ImageDraw
from datetime import*
import time
from math import *
import sqlite3
import os

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg= "#021e2f")

        left_lbl = Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)
        right_lbl = Label(self.root,bg="#031f3c",bd=0)
        right_lbl.place(x=600,y=0,relheight=1,relwidth=1)

        login_frame = Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)

        title=Label(login_frame,text="Login Here",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=50)
        
        email=Label(login_frame,text="Email Address:",font=("times new roman",18,"bold"),bg="white",fg="Black").place(x=250,y=150)
        self.txt_email=Entry(login_frame,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_email.place(x=250,y=180,width=390,height=35)

        password=Label(login_frame,text="Password:",font=("times new roman",18,"bold"),bg="white",fg="Black").place(x=250,y=250)
        self.txt_password=Entry(login_frame,font=("times new roman",15,"bold"),bg="lightgray")
        self.txt_password.place(x=250,y=280,width=390,height=35)

        btn_reg = Button(login_frame,text="Register new Account?",font=("times new roman",14),cursor="hand2",bg="white",bd=0,fg="#b00857",command=self.register_window).place(x=250,y=320)
        btn_forget = Button(login_frame,text="Forget Password?",font=("times new roman",14),cursor="hand2",bg="white",bd=0,fg="red",command=self.forget_password_window).place(x=500,y=320)
        btn_login = Button(login_frame,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#b00857",cursor="hand2",command=self.login).place(x=250,y=380,width=180,height=40)

        self.lbl=Label(self.root,text="Hi All",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=90,y=120,height=450,width=350)
        self.working()

    def reset(self):
        self.cmb_quest.current(0)
        self.txt_new_password.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)

    def forget_password(self):
        if self.cmb_quest.get() == "Select" or self.txt_answer.get()=="" or self.txt_new_password=="":
            messagebox.showerror("Error","All fields are required",parent=self.root2)
        else:
            try:
                con=con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and question=? and answer=?",(self.txt_email.get(),self.cmb_quest.get(),self.txt_answer.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please Select the correct Security Question / Enter Answer",parent=self.root2)
                else:
                    cur.execute("update employee set password=? where email=?",(self.txt_new_password.get(),self.txt_email.get(),))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Your password has been reset, Please login with new password",parent=self.root2)
                    self.reset()
                    self.root2.destroy
            except Exception as es:       
                    messagebox.showerror("Error",f"Error Due to: {str(es)}", parent=self.root)
        
    def forget_password_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password",parent=self.root)
        else:
            try:
                con=con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please enter the valid email address to reset your password",parent=self.root2)
                else:
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("350x400+495+150")
                    self.root2.config(bg="white")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    title=Label(self.root2,text="Forget Password",font=("times new roman",15,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)                    
                    question= Label(self.root2,text="Security Question:",font=("times new roman",15,"bold"),bg="white",fg="Black").place(x=50,y=80)                    
                    self.cmb_quest= ttk.Combobox(self.root2,font=("times new roman",13),state='readonly',justify=CENTER)
                    self.cmb_quest['values'] = ("Select","Your First Name","Your Birth Place","Your Best Friend Name")
                    self.cmb_quest.place(x=50,y=110,width=250,height=30)
                    self.cmb_quest.current(0)
                    answer= Label(self.root2,text="Answer:",font=("times new roman",15,"bold"),bg="white",fg="Black").place(x=50,y=150)
                    self.txt_answer = Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_answer.place(x=50,y=180,width=250,height=30)
                    new_password= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=220)
                    self.txt_new_password = Entry(self.root2,font=("times new roman",15),bg="lightgray")
                    self.txt_new_password.place(x=50,y=250,width=250,height=30)
                    btn_change_password=Button(self.root2,command=self.forget_password,text="Reset Password",bg="green",fg="white",font=("ties new roman",15,"bold")).place(x=80,y=320)
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}", parent=self.root)

    def register_window(self):
        self.root.destroy()
        import register

    def login(self):
        if self.txt_email.get() == "" or self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database="rms.db")
                cur=con.cursor()
                cur.execute("select * from employee where email=? and password=?",(self.txt_email.get(),self.txt_password.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid USERNAME & PASSWORD",parent=self.root)
                else:
                    messagebox.showinfo("Success",f"Welcome: {self.txt_email.get()}",parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}",parent=self.root)

    def clock_image(self,hr,min_,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)

        bg = Image.open("images/c.png")
        bg = bg.resize((300,300),Image.BILINEAR)
        clock.paste(bg,(50,50))

        # angle_in_radians = angle_in_radians * math.pi / 180
        # line_length = 100
        # center_x = 250
        # center_y = 250
        # end_x = centre_x + line_length * math.cos(angle_in_radians)
        # end_y = centre_y + line_length * math.sin(angle_in_radians)

        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#df005e",width=4)
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="yellow",width=2)
        draw.ellipse((195,195,210,210),fill="#1AD5D5")
        clock.save("images/clock_new.png")

    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        hr=(h/12)*360
        min_ = (m/60)*360
        sec_ = (s/60)*360
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

root = Tk()
obj = Login_window(root)
root.mainloop()