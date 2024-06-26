import cv2
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

class About_Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x816+0+0")
        self.root.title("About Developer")

        img_1=Image.open("Images//dev.jpg")
        img_1=img_1.resize((800,200),Image.ANTIALIAS)
        self.lfimg=ImageTk.PhotoImage(img_1)

        f_lbl=Label(root,image=self.lfimg)
        f_lbl.place(x=0,y=0,width=800,height=200)

        img_2=Image.open("Images//develop1.jpg")
        img_2=img_2.resize((800,200),Image.ANTIALIAS)
        self.img2=ImageTk.PhotoImage(img_2)

        f_lbl=Label(root,image=self.img2)
        f_lbl.place(x=800,y=0,width=800,height=200)


        title_lbl=Label(root,text="ABOUT DEVELOPER",font=("times new roman",40,"bold"),bg="light blue",fg="black")
        title_lbl.place(x=0,y=202,width=1536,height=50)


        img_3=Image.open("Images//developer.png")
        img_3=img_3.resize((790,566),Image.ANTIALIAS)
        self.img3=ImageTk.PhotoImage(img_3)

        f_lbl=Label(root,image=self.img3)
        f_lbl.place(x=0,y=254,width=790,height=566)

        main_frame=Frame(root,bd=2,bg="white")
        main_frame.place(x=790,y=254,width=735,height=566)

        dev_lbl=Label(main_frame,text="Hello ! My name is Suryansh Upadhyay.",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        dev_lbl.place(x=0,y=170,width=730,height=50)

        dev1_lbl=Label(main_frame,text="I am interested in Data Science and DSA.",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        dev1_lbl.place(x=0,y=220,width=730,height=50)
        
        dev2_lbl=Label(main_frame,text="Hey ! My name is Vaibhav Pandey.",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        dev2_lbl.place(x=0,y=320,width=730,height=50)

        dev2_lbl2=Label(main_frame,text="I am interested in Web Development.",font=("times new roman",20,"bold"),bg="light blue",fg="black")
        dev2_lbl2.place(x=0,y=370,width=730,height=50)



if __name__ == "__main__":
    root = Tk()
    obj=About_Developer(root)
    root.mainloop()            