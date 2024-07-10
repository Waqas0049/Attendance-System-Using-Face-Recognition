from tkinter import *
from PIL import Image, ImageTk
import tkinter
from db.student import Student
import os
from train import Train
from face_recognition import FaceRecognitionApp
from face_recognition import FaceRecognitionApp
from attendance_record import AttendanceRecord
from developer import Developer
from help import Help
from time import strftime
from student import Student


class Face_recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size and position
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Top Images
        img = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\1.jpg")
        img = img.resize((500, 130), )
        self.photoimg = ImageTk.PhotoImage(img)
        f_Ibl = Label(self.root, image=self.photoimg)
        f_Ibl.place(x=0, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\1.jpg")
        img2 = img2.resize((500, 130), )
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_Ibl = Label(self.root, image=self.photoimg2)
        f_Ibl.place(x=500, y=0, width=500, height=130)

        img4 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\1.jpg")
        img4 = img4.resize((500, 130), )
        self.photoimg4 = ImageTk.PhotoImage(img4)
        f_Ibl = Label(self.root, image=self.photoimg4)
        f_Ibl.place(x=900, y=0, width=500, height=130)

        # BackGround Image

        img5 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\back2.jpg")
        img5 = img5.resize((1530, 710), )
        self.photoimg5 = ImageTk.PhotoImage(img5)
        bg_img = Label(self.root, image=self.photoimg5)
        bg_img.place(x=0, y=130, width=1530, height=710)

        # title face attendance system

        title_Ibl = Label(bg_img, text="FACE ATTENDANCE SYSTEM DEPARTMENT OF CS&IT",
                          font=("times new roman", 25, "bold"), foreground="RED", background="BLACK")
        title_Ibl.place(x=0, y=0, width=1380, height=50)
        # Student Button
        img6 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\stud.jpg")
        img6 = img6.resize((200, 130), )
        self.photoimg6 = ImageTk.PhotoImage(img6)

        # Time

        def time():
            string = strftime("%H:%M:%S %p")
            Ibl.config(text=string)
            Ibl.after(1000, time)

        Ibl = Label(title_Ibl, font=("times new roman", 14, "bold"), background="black", fg="Red")
        Ibl.place(x=5, y=10, width=100, height=50)
        time()

        # Student Button

        b1 = Button(bg_img, image=self.photoimg6, command=self.studend_details, cursor="hand2")
        b1.place(x=100, y=70, width=200, height=160)

        b1_1 = Button(bg_img, text="Student Detials", command=self.studend_details, cursor="hand2",
                      font=("times new roman", 15, "bold"), foreground="black", background="#d77337")
        b1_1.place(x=100, y=230, width=200, height=40)

        # Face Detector

        img7 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\face.jpg")
        img7 = img7.resize((200, 160), )
        self.photoimg7 = ImageTk.PhotoImage(img7)
        b2 = Button(bg_img, image=self.photoimg7, cursor="hand2", command=self.face_data)
        b2.place(x=400, y=70, width=200, height=160)

        b1_2 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data,
                      font=("times new roman", 15, "bold"),
                      foreground="black", background="#d77337")
        b1_2.place(x=400, y=230, width=200, height=40)

        # Attendance Button
        img8 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\attend.jpg")
        img8 = img8.resize((200, 160), )
        self.photoimg8 = ImageTk.PhotoImage(img8)
        b3 = Button(bg_img, image=self.photoimg8, cursor="hand2", command=self.attendance_data)
        b3.place(x=700, y=70, width=200, height=160)

        b1_3 = Button(bg_img, text="Attendance", command=self.attendance_data, cursor="hand2",
                      font=("times new roman", 15, "bold"),
                      foreground="black", background="#d77337")
        b1_3.place(x=700, y=230, width=200, height=40)

        # Help Disk Button

        img9 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\help.jpg")
        img9 = img9.resize((200, 160), )
        self.photoimg9 = ImageTk.PhotoImage(img9)
        b4 = Button(bg_img, image=self.photoimg9, cursor="hand2", command=self.help_data)
        b4.place(x=1000, y=70, width=200, height=160)

        b1_4 = Button(bg_img, text="Help", command=self.help_data, cursor="hand2", font=("times new roman", 15, "bold"),
                      foreground="black", background="#d77337")
        b1_4.place(x=1000, y=230, width=200, height=40)

        # Train Data Button

        img10 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\train.jpg")
        img10 = img10.resize((200, 160), )
        self.photoimg10 = ImageTk.PhotoImage(img10)
        b5 = Button(bg_img, image=self.photoimg10, cursor="hand2", command=self.train_data)
        b5.place(x=100, y=330, width=200, height=160)

        b1_5 = Button(bg_img, text="Train Data", cursor="hand2", command=self.train_data,
                      font=("times new roman", 15, "bold"),
                      foreground="black", background="#d77337")
        b1_5.place(x=100, y=480, width=200, height=40)

        # Photo Button
        img11 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\photo.jpg")
        img11 = img11.resize((200, 160), )
        self.photoimg11 = ImageTk.PhotoImage(img11)
        b6 = Button(bg_img, image=self.photoimg11, cursor="hand2", command=self.open_img)
        b6.place(x=400, y=330, width=200, height=160)

        b1_6 = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 15, "bold"),
                      foreground="black", background="#d77337")
        b1_6.place(x=400, y=480, width=200, height=40)

        # Developer Button

        img12 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\developer.jpg")
        img12 = img12.resize((200, 160), )
        self.photoimg12 = ImageTk.PhotoImage(img12)
        b7 = Button(bg_img, image=self.photoimg12, cursor="hand2", command=self.developer_data)
        b7.place(x=700, y=330, width=200, height=160)

        b1_7 = Button(bg_img, text="Developer", command=self.developer_data, cursor="hand2",
                      font=("times new roman", 15, "bold"),
                      foreground="black", background="#d77337")
        b1_7.place(x=700, y=480, width=200, height=40)

        # Exit Button
        img13 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\exit.jpg")
        img13 = img13.resize((200, 160), )
        self.photoimg13 = ImageTk.PhotoImage(img13)
        b7 = Button(bg_img, image=self.photoimg13, cursor="hand2", command=self.exit)
        b7.place(x=1000, y=330, width=200, height=160)

        b1_7 = Button(bg_img, text="Exit", cursor="hand2", command=self.exit, font=("times new roman", 15, "bold"),
                      foreground="black", background="#d77337")
        b1_7.place(x=1000, y=480, width=200, height=40)

    def open_img(self):
        os.startfile("data_set")

    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Exit", "Are you sure exit this project", parent=self.root)
        if self.exit > 0:
            self.root.destroy()
        else:
            return

        # Function Button

    def studend_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognitionApp(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = AttendanceRecord(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.new_window = Help(self.new_window)

    def FaceRecognitionApp(self):
        self.new_window = Toplevel(self.root)
        self.new_window = Help(self.new_window)



if __name__ == '__main__':
    root = Tk()
    app = Face_recognition_System(root)
    root.mainloop()
