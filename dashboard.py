from tkinter import *
from PIL import Image,ImageTk,ImageDraw
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import ttk, messagebox
import os
from datetime import*
import time
from math import *
import sqlite3

class Rms:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1520x780+0+0")
        self.root.config(bg="light yellow")

        self.logo_dash = ImageTk.PhotoImage(file="images/logo_p.png")

        title=Label(self.root, text="Student Result Management System", padx=10, compound=LEFT, image=self.logo_dash, font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0, y=0, relwidth=1, height=50 )

        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10,y=60, width=1500, height=70)

        btn_course = Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=20, y=5, width=200, height=35)
        btn_student = Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=240, y=5, width=200, height=35)
        btn_result = Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_result).place(x=460, y=5, width=200, height=35)
        btn_view = Button(M_Frame, text="View", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white", cursor="hand2",command=self.add_report).place(x=680, y=5, width=200, height=35)
        btn_logout = Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.logout).place(x=900, y=5, width=200, height=35)
        btn_exit = Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#0b5377", fg="white",cursor="hand2",command=self.exit_).place(x=1120, y=5, width=200, height=35)

        self.bl_image = Image.open("images/3.jpg")
        self.bl_image = self.bl_image.resize((960,600),Image.BILINEAR)
        self.bl_image = ImageTk.PhotoImage(self.bl_image)
        self.lbl_image = Label(self.root,image=self.bl_image).place(x=400,y=180,width=920,height=350)
        
        self.lbl_course = Label(self.root,text="ToTal Courses\n [0]", font=("goudy old style", 20),bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)
        self.lbl_student = Label(self.root, text="ToTal Students\n [0]", font=("goudy old style", 20), bd=10,relief=RIDGE, bg="#e676ad", fg="white")
        self.lbl_student.place(x=710, y=530, width=300, height=100)
        self.lbl_result = Label(self.root, text="ToTal Results\n [0]", font=("goudy old style", 20), bd=10,relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1020, y=530, width=300, height=100)

        self.lbl=Label(self.root,text="Hi All",font=("Book Antiqua",25,"bold"),fg="white",compound=BOTTOM,bg="#081923",bd=0)
        self.lbl.place(x=10,y=180,height=450,width=370)
        self.working()

        footer = Label(self.root, text="Student Result Management System\nContact us for any technical issue: 9345623212 - matheenroy@gmail.com", font=("goudy old style", 12, "bold"), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
        self.update_details()

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

    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")            
            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")            
            self.lbl_course.after(200,self.update_details)            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

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
        
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to Exit?",parent=self.root)
        if op == True:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Rms(root)
    root.mainloop()