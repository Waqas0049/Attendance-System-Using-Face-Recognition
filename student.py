from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

import face_recognition_models
import os
from train import Train


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student")
        self.root.geometry("1300x750+0+0")

        # Variable
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        # Top Images
        img = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\back.jpg")
        img = img.resize((500, 100), )
        self.photoimg = ImageTk.PhotoImage(img)
        f_Ibl = Label(self.root, image=self.photoimg)
        f_Ibl.place(x=0, y=0, width=500, height=100)

        img2 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\back.jpg")
        img2 = img2.resize((500, 130), )
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_Ibl = Label(self.root, image=self.photoimg2)
        f_Ibl.place(x=300, y=0, width=500, height=100)

        img3 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\back.jpg")
        img3 = img3.resize((500, 130), )
        self.photoimg3 = ImageTk.PhotoImage(img3)
        f_Ibl = Label(self.root, image=self.photoimg3)
        f_Ibl.place(x=600, y=0, width=500, height=100)

        img4 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\back.jpg")
        img4 = img4.resize((500, 130), )
        self.photoimg4 = ImageTk.PhotoImage(img4)
        f_Ibl = Label(self.root, image=self.photoimg4)
        f_Ibl.place(x=900, y=0, width=500, height=100)

        # Background Image
        img5 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\back2.jpg")
        img5 = img5.resize((1530, 710), )
        self.photoimg5 = ImageTk.PhotoImage(img5)
        bg_img = Label(self.root, image=self.photoimg5)
        bg_img.place(x=0, y=100, width=1530, height=710)

        # title face attendance system
        title_Ibl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 30, "bold"), foreground="#EC5800", background="#F0F8FF")
        title_Ibl.place(x=0, y=0, width=1400, height=45)

        # Mian Frame
        main_frame = Frame(bg_img, bd=2, bg="#3B00DB")
        main_frame.place(x=0, y=50, width=1400, height=700)

        # Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 12, "bold"), bg="#E25822")
        Left_frame.place(x=10, y=4, width=670, height=540)

        # Top Image
        img6 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\back.jpg")
        img6 = img6.resize((670, 130), )
        self.photoimg6 = ImageTk.PhotoImage(img6)
        f_Ibl = Label(Left_frame, image=self.photoimg6)
        f_Ibl.place(x=0, y=0, width=670, height=100)

        # Current Course
        current_course_frame = LabelFrame(Left_frame, bd=2, text="Course Information Details ",
                                          font=("times new roman", 12, "bold"), bg="white")
        current_course_frame.place(x=5, y=105, width=660, height=100)

        # Department Label
        dep_label = Label(current_course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0)

        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, font=("times new roman", 12, "bold"),
                                 width=22, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "IT",)
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=5)

        # Course Label
        course_label = Label(current_course_frame, text="Select Course", font=("times new roman", 12, "bold"),
                             bg="white")
        course_label.grid(row=0, column=2, padx=5, pady=5)

        course_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course,
                                    font=("times new roman", 12, "bold"), width=22, state="readonly")
        course_combo["values"] = (
        "Select Course", "English", "Information Security", "Data Structure", "Web Design", "Python", "Cyber Security")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=5, pady=5)

        # Year
        year_label = Label(current_course_frame, text="Select Year", font=("times new roman", 12, "bold"), bg="white", )
        year_label.grid(row=1, column=0, padx=10, pady=5)

        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year,
                                  font=("times new roman", 12, "bold"), width=22, state="readonly")
        year_combo["values"] = ("Select Year", "2020", "2021", "2022", "2023", "2024")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=5, pady=5)

        # Semester
        semester_label = Label(current_course_frame, text="Select Semester", font=("times new roman", 12, "bold"),
                               bg="white")
        semester_label.grid(row=1, column=2, padx=5, pady=5)
        semester_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester,
                                      font=("times new roman", 12, "bold"), width=22,
                                      state="readonly")
        semester_combo["values"] = ("Select Semester", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=5, pady=5)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame, bd=2, bg="white", text="Class Student Information",
                                         font=("times new roman", 12, "bold"))
        class_student_frame.place(x=5, y=210, width=660, height=300)

        # Student Id
        studentId_label = Label(class_student_frame, text="StudentID:", font=("times new roman", 12, "bold"),
                                bg="white")
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_id,
                                    font=("times new roman", 12, "bold"), width=22)
        studentID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label = Label(class_student_frame, text="Student Name: ", font=("times new roman", 12, "bold"),
                                  bg="white")
        studentName_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        studentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_std_name,
                                      font=("times new roman", 12, "bold"), width=22)
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class Division
        class_div_label = Label(class_student_frame, text="Class Division: ", font=("times new roman", 12, "bold"),
                                bg="white")
        class_div_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(class_student_frame, textvariable=self.var_div,
                                       font=("times new roman", 12, "bold"), width=20,
                                       state="readonly")
        class_div_combo["values"] = ("Select Division", "A", "B", "C",)
        class_div_combo.current(0)
        class_div_combo.grid(row=1, column=1, padx=5, pady=5)

        # Roll No
        roll_no_label = Label(class_student_frame, text="Roll No: ", font=("times new roman", 12, "bold"),
                              bg="white")
        roll_no_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        roll_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, font=("times new roman", 12, "bold"),
                                  width=22)
        roll_no_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text="Gender:", font=("times new roman", 12, "bold"),
                             bg="white")
        gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        gender_combo = ttk.Combobox(class_student_frame, textvariable=self.var_gender,
                                    font=("times new roman", 12, "bold"), width=20,
                                    state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other",)
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5)

        # DOB
        dob_label = Label(class_student_frame, text="DOB: ", font=("times new roman", 12, "bold"),
                          bg="white")
        dob_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        dob_entry = ttk.Entry(class_student_frame, textvariable=self.var_dob, font=("times new roman", 12, "bold"),
                              width=22)
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text="Email: ", font=("times new roman", 12, "bold"),
                            bg="white")
        email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_email, font=("times new roman", 12, "bold"),
                                width=22)
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone No
        phone_label = Label(class_student_frame, text="Phone No: ", font=("times new roman", 12, "bold"),
                            bg="white")
        phone_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        phone_entry = ttk.Entry(class_student_frame, textvariable=self.var_phone, font=("times new roman", 12, "bold"),
                                width=22)
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text="Address: ", font=("times new roman", 12, "bold"),
                              bg="white")
        address_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_address,
                                  font=("times new roman", 12, "bold"), width=22)
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name
        teacher_label = Label(class_student_frame, text="Techer: ", font=("times new roman", 12, "bold"),
                              bg="white")
        teacher_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        teacher_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacher,
                                  font=("times new roman", 12, "bold"), width=22)
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        # Radio Button Take A Photo Sample
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="Take Photo Sample",
                                    value="Yes", )
        radiobtn1.grid(row=5, column=0, padx=5, pady=10)

        radiobtn2 = ttk.Radiobutton(class_student_frame, variable=self.var_radio1, text="No Photo Sample", value="No")
        radiobtn2.grid(row=5, column=1, padx=5, pady=10)

        # Button Frame in Class Student Frame
        btn_frame = Frame(class_student_frame, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=210, width=655, height=65)

        # Save Button
        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=22, font=("times new roman", 10, "bold"),
                          foreground="black",
                          background="#d77337", )
        save_btn.grid(row=0, column=0)

        # Update Button
        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=22,
                            font=("times new roman", 10, "bold"), foreground="black",
                            background="#d77337", )
        update_btn.grid(row=0, column=1)

        # Delete Button
        delete_btn = Button(btn_frame, text="Delete", command=self.delete_data, width=22,
                            font=("times new roman", 10, "bold"), foreground="black",
                            background="#d77337", )
        delete_btn.grid(row=0, column=2)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=22,
                           font=("times new roman", 10, "bold"), foreground="black",
                           background="#d77337", )
        reset_btn.grid(row=0, column=3)

        # Button Frame 1
        btn_frame1 = Frame(btn_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0, y=25, width=660, height=35)

        take_photo_btn = Button(btn_frame1, command=self.generate_dataset, text="Take Photo Sample", width=45,
                                font=("times new roman", 10, "bold"),
                                foreground="black",
                                background="#d77337", )
        take_photo_btn.grid(row=0, column=0)

        # Update Photo button

        update_photo_btn = Button(btn_frame1, text="Update Photo Sample", width=45,
                                  font=("times new roman", 10, "bold"),
                                  foreground="black",
                                  background="#d77337", )
        update_photo_btn.grid(row=0, column=1)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student ", font=("times new roman", 12, "bold"),
                                 bg="#E25822")
        Right_frame.place(x=685, y=4, width=670, height=540)

        img7 = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\back.jpg")
        img7 = img6.resize((670, 130), )
        self.photoimg7 = ImageTk.PhotoImage(img7)
        f_Ibl = Label(Right_frame, image=self.photoimg6)
        f_Ibl.place(x=0, y=0, width=670, height=100)

        # Search system Frame
        search_frame = LabelFrame(Right_frame, bd=2, text="Search System ",
                                  font=("times new roman", 12, "bold"), bg="white")
        search_frame.place(x=5, y=105, width=660, height=100)

        saerch_label = Label(search_frame, text="Search By: ", font=("times new roman", 12, "bold"),
                             bg="Red", fg="White")
        saerch_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame, font=("times new roman", 12, "bold"), width=10,
                                    state="readonly")
        search_combo["values"] = ("Select", "Phone No", "Roll No",)
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, pady=5)

        search_entry = ttk.Entry(search_frame, font=("times new roman", 12, "bold"), width=20)
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_frame, text="Search", width=15, font=("times new roman", 10, "bold"),
                            foreground="black",
                            background="#d77337", )
        search_btn.grid(row=0, column=3)

        showAll_btn = Button(search_frame, text="Show All", width=15, font=("times new roman", 10, "bold"),
                             foreground="black",
                             background="#d77337", )
        showAll_btn.grid(row=0, column=4)

        # Table Frame
        table_frame = LabelFrame(Right_frame, bd=2, bg="white",
                                 font=("times new roman", 12, "bold"))
        table_frame.place(x=5, y=210, width=660, height=300)

        # Scroll
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "div",
                                                                "roll", "gender", "dob", "email", "phone", "address",
                                                                "teacher", "photo"), xscrollcommand=scroll_x.set,
                                          yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("roll", text="Roll")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")

        self.student_table["show"] = "headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

        # function Declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fileds are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="03493674002",
                                               database="fyp")
                mycursor = conn.cursor()
                mycursor.execute("INSERT INTO student_data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully ", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

        # Fetch Data

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="03493674002",
                                       database="fyp")
        mycursor = conn.cursor()
        mycursor.execute("SELECT * FROM student_data")
        data = mycursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        # Get Course

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

        # Update Functio

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                Upodate = messagebox.askyesno("Update", "Do you want to update this student", parent=self.root)
                if Upodate > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="03493674002",
                                                   database="fyp")
                    mycursor = conn.cursor()
                    mycursor.execute(
                        "UPDATE student_data  SET Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                        (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        ))

                else:
                    if not Upodate:
                        return
                messagebox.showinfo("Success", "Student details successfully update completed",
                                    parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # Delete Function

    # Delete Function
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                Delete = messagebox.askyesno("Delete", "Do you want to delete this student", parent=self.root)
                if Delete > 0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="03493674002",
                                                   database="fyp")
                    mycursor = conn.cursor()
                    sql = "DELETE FROM student_data WHERE Student_id=%s"
                    val = (self.var_std_id.get(),)
                    mycursor.execute(sql, val)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # Reset Function
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    # Generate Dataset / Take Photo Sample
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="03493674002",
                                               database="fyp")
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM student_data")
                myresult = mycursor.fetchall()
                id = 0
                for x in myresult:
                    id += 1
                mycursor.execute(
                    "UPDATE student_data SET Dep=%s, course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get() == id + 1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from opencv
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling factor=1.3
                    # Minimum neighbor=5
                    for (x, y, w, h) in faces:
                        cropped_face = img[y:y + h, x:x + w]
                        return cropped_face

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
