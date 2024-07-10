from  tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import  messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import  filedialog


class Developer:
    def __init__(self, root):
        self.root=root
        self.root.title("Developer")

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size and position
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1400, height=40)

        img_bg = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\developer.jpg")
        img_bg= img_bg.resize((1400, 700))
        self.Photoimg_bg= ImageTk.PhotoImage(img_bg)

        f_lbl = Label(self.root, image=self.Photoimg_bg)
        f_lbl.place(x=0, y=50, width=1400, height=700)

        # Frame
        main_frame=Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=800, y=55, width=500, height=500)

        img = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\waqas.jpg")
        img = img.resize((200, 200))
        self.Photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(main_frame, image=self.Photoimg)
        f_lbl.place(x=300, y=0, width=200, height=200)

        # Developer Information

        dep_Label= Label(main_frame, text="Hello,", font=("times new roman", 20, "bold"), bg="white")
        dep_Label.place(x=10, y=10)
        dep_Label1 = Label(main_frame, text="I Am Waqas Ahmad", font=("times new roman", 20, "bold"), bg="white")
        dep_Label1.place(x=10, y=50)
        dep_Label2 = Label(main_frame, text="Python Developer ", font=("times new roman", 20, "bold"), bg="white", fg="blue")
        dep_Label2.place(x=10, y=80)
        dep_Label3 = Label(main_frame, text="Education:", font=("times new roman", 20, "bold"), bg="white")
        dep_Label3.place(x=10, y=110)
        dep_Label4 = Label(main_frame, text="BS Computer Science ", font=("times new roman", 20, "bold"), bg="white")
        dep_Label4.place(x=10, y=140)
        dep_Label5 = Label(main_frame, text="University Of Malakand", font=("times new roman", 20, "bold"), bg="white", fg="red")
        dep_Label5.place(x=10, y=180)
        dep_Label6 = Label(main_frame, text="Whatsapp: 03493674002", font=("times new roman", 20, "bold"), bg="white",
                           fg="red")
        dep_Label6.place(x=10, y=210)
        dep_Label7 = Label(main_frame, text="Email: waqasuom9@gmail.com", font=("times new roman", 20, "bold"), bg="white",
                           fg="red")
        dep_Label7.place(x=10, y=250)




if __name__ == "__main__":
    root=Tk()
    app=Developer(root)
    root.mainloop()

