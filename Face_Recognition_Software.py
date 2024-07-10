from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
from db import student
from tkinter import messagebox
import os
from train import Train
from face_recognition import FaceRecognitionApp
from attendance_record import AttendanceRecord
from developer import Developer
from help import Help
from time import strftime
import mysql.connector

def main():
    win=Tk()
    app=Login(win)
    win.mainloop()

class Login:
    def __init__(self, root):
        self.root2 = None
        self.root = root
        self.root.title("Login System")



        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size and position
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        self.bg = ImageTk.PhotoImage(file=r'C:\Users\Waqas Ahmad\Desktop\images\loginbg.jpg')
        self.bg_image = Label(self.root, image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        Frame_login = Frame(self.root, bg="white")
        Frame_login.place(x=150, y=150, height=370, width=500)

        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="#d77337", bg="white")
        title.place(x=90, y=30)
        desc = Label(Frame_login, text="Welcome To Face Attendnace System", font=("Goudy old style", 15, "bold"), fg="#d25d17", bg="white")
        desc.place(x=90, y=100)

        Ibl_user = Label(Frame_login, text="Username", font=("Goudy old style", 15, "bold"), fg="Gray", bg="white")
        Ibl_user.place(x=90, y=140)
        self.txt_user = Entry(Frame_login, font=("times new roman ", 15, "bold"), bg="lightgray")
        self.txt_user.place(x=90, y=170, width=350, height=35)

        Ibl_pass = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="Gray", bg="white")
        Ibl_pass.place(x=90, y=210)
        self.txt_pass = Entry(Frame_login, font=("times new roman ", 15, "bold"), bg="lightgray")
        self.txt_pass.place(x=90, y=240, width=350, height=35)

        forgot_btn = Button(Frame_login, text="Forgot Password", command=self.forgot_pass_window, cursor="hand2", bd=0, bg="white", fg="#d77337", font=("times new roman", 12))
        forgot_btn.place(x=320, y=280)

        registration_btn = Button(Frame_login, command=self.register_window, text="New Registration", cursor="hand2", bd=0, bg="white", fg="#d77337", font=("times new roman", 12))
        registration_btn.place(x=320, y=305)

        Login_btn = Button(self.root, command=self.Login_function, cursor="hand2", text="Login", bd=0, bg="#d77337", fg="white", font=("times new roman", 20))
        Login_btn.place(x=300, y=500, width=180, height=40)

    def register_window(self):
        self.new_window = Toplevel(self.root)
        app = RegistrationForm(self.new_window)

    def Login_function(self):
        if self.txt_user.get() == "" or self.txt_pass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.txt_user.get() == "waqas" and self.txt_pass.get() == "123":
            messagebox.showinfo("Success", "Welcome to Face Attendance System", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="03493674002",
                database="fyp"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM registration WHERE email=%s and password=%s", (
                self.txt_user.get(),
                self.txt_pass.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username & Password", parent=self.root)
            else:
                open_main = messagebox.askyesno("YesNO", "Access only admin", parent=self.root)
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = Face_recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
                conn.commit()
                conn.close()

        # Reset Password

    def reset_password(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error", "Select the security questtion ?",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error", "Please enter the answer!",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error", "Please enter the new password ",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost", username="root", password="03493674002", database="my_project")
            my_cursor=conn.cursor()
            query=("SELECT * FROM registration WHERE email=%s and securityQ=%s and securityA=%s")
            value=(self.txt_user.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Please enter the correct answer",parent=self.root2)
            else:
                query=("UPDATE registration SET password=%s WHERE email=%s")
                value=(self.txt_newpass.get(), self.txt_user.get())
                my_cursor.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Information", "Your password has been reset, please login new password",parent=self.root2)
                self.root2.destroy()


        # Forgot Password Page

    def forgot_pass_window(self,):
        if self.txt_user.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset your password", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="03493674002", database="fyp")
            my_cursor = conn.cursor()
            query = "SELECT * FROM registration WHERE email=%s"
            value = (self.txt_user.get(),)
            my_cursor.execute(query, value)

            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "Please enter the valid username", parent=self.root)
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("380x380+600+180")

                l=Label(self.root2, text="Forgot Password", font=("times new roman", 20, "bold"), fg="red", bg="orange")
                l.place(x=0, y=10,relwidth=1, )
                security_Q = Label(self.root2, text="Select Security Question",
                                   font=("times new roman", 15, "bold"), foreground="black",
                                   background="white")
                security_Q.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2,
                                                     font=("times new roman", 15, "bold"), state="readonly", width=23)
                self.combo_security_Q["values"] = (
                "Select", "Your Birth Place?", "Your favorite Color?", "Your Pet Name?")
                self.combo_security_Q.place(x=50, y=110)
                self.combo_security_Q.current(0)

                # Select Answer
                security_A = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"),
                                   foreground="black",
                                   background="white")
                security_A.place(x=50, y=150)
                self.txt_security = ttk.Entry(self.root2,
                                              font=("times new roman", 15, "bold"), )
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="Enter New Password", font=("times new roman", 15, "bold"),
                                   foreground="black",
                                   background="white")
                new_password.place(x=50, y=220)
                self.txt_newpass = ttk.Entry(self.root2,
                                              font=("times new roman", 15, "bold"), )
                self.txt_newpass.place(x=50, y=250, width=250)

                # Button
                btn=Button(self.root2, text="Reset",command=self.reset_password, font=("times new roman", 15, "bold"), fg="white", bg="green")
                btn.place(x=50, y=290, width=250, height=40)





class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1300x670+0+0")

        # Text Variable
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Waqas Ahmad\Desktop\images\loginbg.jpg")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        registration_frame = Frame(self.root, bg="white")
        registration_frame.place(x=110, y=100, height=600, width=800)

        self.label_heading = ttk.Label(registration_frame, text="Registration Here", font=("Impact", 35, "bold"), foreground="#d77337", background="white")
        self.label_heading.place(x=40, y=20)

        # Form Fields
        # First Name
        fname=Label(registration_frame, text="First name", font=("times new roman", 15, "bold"), foreground="black", background="white")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(registration_frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"), )
        fname_entry.place(x=50, y=130, width=250)

        # Last Name
        l_name = Label(registration_frame,text="Last name", font=("times new roman", 15, "bold"), foreground="black",
                      background="white")
        l_name.place(x=330, y=100)
        self.txt_lname= ttk.Entry(registration_frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"), )
        self.txt_lname.place(x=330, y=130, width=250)

        # Conatct No
        contact = Label(registration_frame, text="Contact No", font=("times new roman", 15, "bold"), foreground="black",
                       background="white")
        contact.place(x=50, y=170)
        self.txt_contact = ttk.Entry(registration_frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"), )
        self.txt_contact.place(x=50, y=200, width=250)

        # Email

        email = Label(registration_frame, text="Email", font=("times new roman", 15, "bold"), foreground="black",
                       background="white")
        email.place(x=330, y=170)
        self.txt_email = ttk.Entry(registration_frame, textvariable=self.var_email, font=("times new roman", 15, "bold"), )
        self.txt_email.place(x=330, y=200, width=250)

        # Security Question
        security_Q = Label(registration_frame, text="Select Security Question", font=("times new roman", 15, "bold"), foreground="black",
                      background="white")
        security_Q.place(x=50, y=240)

        self.combo_security_Q=ttk.Combobox(registration_frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly", width=23)
        self.combo_security_Q["values"]=("Select", "Your Birth Place?","Your favorite Color?", "Your Pet Name?")
        self.combo_security_Q.place(x=50, y=270)
        self.combo_security_Q.current(0)

        # Select Answer
        security_A= Label(registration_frame, text="Security Answer", font=("times new roman", 15, "bold"),
                      foreground="black",
                      background="white")
        security_A.place(x=330, y=240)
        self.txt_security = ttk.Entry(registration_frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"), )
        self.txt_security.place(x=330, y=270, width=250)

        # Password
        pswd = Label(registration_frame, text="Password", font=("times new roman", 15, "bold"), foreground="black",
                        background="white")
        pswd.place(x=50, y=310)
        self.txt_pswd = ttk.Entry(registration_frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"), )
        self.txt_pswd.place(x=50, y=340, width=250)

        # Confirm Password
        confirm_pswd= Label(registration_frame, text="Confirm Password", font=("times new roman", 15, "bold"),
                           foreground="black",
                           background="white")
        confirm_pswd.place(x=330, y=310)
        self.txt_confirm_pswd= ttk.Entry(registration_frame, textvariable=self.var_confpass,  font=("times new roman", 15, "bold"), )
        self.txt_confirm_pswd.place(x=330, y=340, width=250)

        # Check button

        self.var_check=IntVar()
        checkbtn=Checkbutton(registration_frame,variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new rowan", 12, "bold"), onvalue=1, offvalue=0)
        checkbtn.place(x=50, y=380)


        # Registration Button

        reg_btn = Button(self.root, command=self.register_data, cursor="hand2", text="Registration", bd=0, bg="#d77337",
                           fg="white",
                           font=("times new roman", 20,)).place(x=190, y=520, width=180, height=40)

        # login Button
        Login_btn = Button(self.root,  command=self.return_login, cursor="hand2", text="Login", bd=0, bg="#d77337",
                       fg="white",
                       font=("times new roman", 20,)).place(x=470, y=520, width=180, height=40)

    def register(self):
        # Perform validation
        if not self.validate_form:
            return

        # Get values from the form
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        contact_no = self.entry_contact_no.get()
        email = self.entry_email.get()
        security_question = self.security_question_var.get()
        security_answer = self.entry_security_answer.get()
        password = self.entry_password.get()

        # Connect to MySQL database
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="03493674002",
                database="fyp"
            )
            cursor = conn.cursor()

            # Insert user data into the database
            query = "INSERT INTO user (firstName, lastName, contactNo, email, securityQuestion, securityAnswer, password) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (first_name, last_name, contact_no, email, security_question, security_answer, password)
            cursor.execute(query, values)

            conn.commit()
            conn.close()

            messagebox.showinfo("Success", "Registration successful!", parent=self.root)
        except mysql.connector.Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    def login(self):
        # Implement your login functionality here
        print("Login button clicked")

    @property
    def validate_form(self):
        # Perform your form validation here
        if not self.entry_first_name.get() or not self.entry_last_name.get() or not self.entry_contact_no.get() \
                or not self.entry_email.get() or not self.entry_security_answer.get() or not self.entry_password.get() \
                or not self.entry_confirm_password.get():
            messagebox.showerror("Error", "All fields are required.")
            return False

        if self.entry_password.get() != self.entry_confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match.")
            return False

        if not self.terms_var.get():
            messagebox.showerror("Error", "Please accept the terms and conditions.")
            return False

        # Add additional validation as needed

        return True

    # Function Declaration

    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error", "All filed are required", parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error", "Password & confirm password must be same", parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Please agree terms and condition", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="03493674002",
                                           database="fyp")
            my_cursor=conn.cursor()
            query=("SELECT * FROM registration WHERE email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "User already exit, Please try another email", parent=self.root)
            else:
                my_cursor.execute("INSERT into registration VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()

                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully", parent=self.root )

    def return_login(self):
        self.root.destroy()


class Face_recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("1300x670+0+0")

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
        self.app = student.Student(self.new_window)


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


def main():
    win = Tk()
    app = Login(win)
    win.mainloop()
if __name__ == "__main__":
    main()
