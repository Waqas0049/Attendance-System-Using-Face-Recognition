from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from PIL import ImageTk

class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size and position
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Text Variable
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()


        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Waqas Ahmad\Desktop\images\back.jpg", )
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
        Login_btn = Button(self.root, command=self.login,  cursor="hand2", text="Login", bd=0, bg="#d77337",
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
           pass

    @property
    def validate_form(self):
        # Perform your form validation here
        if not self.entry_first_name.get() or not self.entry_last_name.get() or not self.entry_contact_no.get() \
                or not self.entry_email.get() or not self.entry_security_answer.get() or not self.entry_password.get() \
                or not self.entry_confirm_password.get():
            messagebox.showerror("Error", "All fields are required.", parent=self.root)
            return False

        if self.entry_password.get() != self.entry_confirm_password.get():
            messagebox.showerror("Error", "Passwords do not match.", parent=self.root)
            return False

        if not self.terms_var.get():
            messagebox.showerror("Error", "Please accept the terms and conditions.", parent=self.root)
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
            messagebox.showinfo("Success", "Register Successfully", parent=self.root)






if __name__ == "__main__":
    root = tk.Tk()
    app = RegistrationForm(root)
    root.mainloop()
