from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata = []

class AttendanceRecord:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Record")
        self.root.geometry("1300x750+0+0")

        # Text Variables
        self.var_atten_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()

        title_lbl = Label(self.root, text="ATTENDANCE REPORT", font=("times new roman", 35, "bold"), foreground="RED", background="BLACK")
        title_lbl.place(x=0, y=0, width=1380, height=50)

        # Background Image
        img_bg = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\attendancer_record.jpg")
        img_bg = img_bg.resize((1400, 790))
        self.PhotoImage = ImageTk.PhotoImage(img_bg)

        img_bg = Label(self.root, image=self.PhotoImage)
        img_bg.place(x=0, y=55, width=1400, height=690)

        # Frame
        main_frame = Frame(img_bg, bd=1, bg="white")
        main_frame.place(x=5, y=10, width=1350, height=630)

        # Left Label Frame
        left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details", font=("times new roman", 12, "bold"), background="white")
        left_frame.place(x=5, y=5, width=680, height=610)

        img_left = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\atten_left_frame.jpg")
        img_left = img_left.resize((665, 130))
        self.Photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame, image=self.Photoimg_left)
        f_lbl.place(x=5, y=5, width=665, height=130)

        left_inside_frame = Frame(left_frame, bd=2, relief=RIDGE, background="White")
        left_inside_frame.place(x=5, y=140, width=665, height=300)

        # Labeled Entry
        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text="Attendance ID:", font=("times new roman", 12, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, textvariable=self.var_atten_id, font=("times new roman", 12, "bold"), width=22)
        attendanceID_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Roll
        roll_label = Label(left_inside_frame, text="Roll NO:", font=("times new roman", 12, "bold"), bg="white")
        roll_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        roll_entry = ttk.Entry(left_inside_frame, textvariable=self.var_attend_roll, font=("times new roman", 12, "bold"), width=22)
        roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Name
        name_label = Label(left_inside_frame, text="Name:", font=("times new roman", 12, "bold"), bg="white")
        name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        name_entry = ttk.Entry(left_inside_frame, textvariable=self.var_attend_name, font=("times new roman", 12, "bold"), width=22)
        name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Department
        department_label = Label(left_inside_frame, text="Department:", font=("times new roman", 12, "bold"), bg="white")
        department_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        department_entry = ttk.Entry(left_inside_frame, textvariable=self.var_attend_dep, font=("times new roman", 12, "bold"), width=22)
        department_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Time
        time_label = Label(left_inside_frame, text="Time:", font=("times new roman", 12, "bold"), bg="white")
        time_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        time_entry = ttk.Entry(left_inside_frame, textvariable=self.var_attend_time, font=("times new roman", 12, "bold"), width=22)
        time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Date
        date_label = Label(left_inside_frame, text="Date:", font=("times new roman", 12, "bold"), bg="white")
        date_label.grid(row=2, column=2, padx=5, pady=5, sticky=W)

        date_entry = ttk.Entry(left_inside_frame, textvariable=self.var_attend_date, font=("times new roman", 12, "bold"), width=22)
        date_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Attendance Combo Box
        atten_label = Label(left_inside_frame, text="Attendance Status:", font=("times new roman", 12, "bold"), background="white")
        atten_label.grid(row=3, column=0)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable=self.var_attend_attendance, width=20, font=("times new roman", 12, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, pady=8)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="black")
        btn_frame.place(x=5, y=230, width=650, height=50)

        # Import csv Button
        import_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=22, font=("times new roman", 10, "bold"), foreground="black", background="#d77337")
        import_btn.grid(row=1, column=0)

        # Export Button
        export_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=22, font=("times new roman", 10, "bold"), foreground="black", background="#d77337")
        export_btn.grid(row=1, column=1)

        # Update Button
        update_btn = Button(btn_frame, text="Update", width=22, font=("times new roman", 10, "bold"), foreground="black", background="#d77337")
        update_btn.grid(row=1, column=2)

        # Reset Button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=22, font=("times new roman", 10, "bold"), foreground="black", background="#d77337")
        reset_btn.grid(row=1, column=3)

        # Right Frame
        right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Details", font=("times new roman", 12, "bold"), background="white")
        right_frame.place(x=690, y=5, width=650, height=610)

        img_right = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\atten_left_frame.jpg")
        img_right = img_right.resize((665, 130))
        self.Photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame, image=self.Photoimg_right)
        f_lbl.place(x=5, y=5, width=665, height=130)

        # Table
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=140, width=630, height=440)

        # Scroll Bar Table
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance Id")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        if fln:
            with open(fln) as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    mydata.append(i)
                self.fetchData(mydata)
        else:
            messagebox.showinfo("Information", "No file selected.", parent=self.root)

    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No Data Found to Export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your Data Exported To " + os.path.basename(fln) + " Successfully", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        if rows:  # Add this check to avoid index error
            self.var_atten_id.set(rows[0])
            self.var_attend_roll.set(rows[1])
            self.var_attend_name.set(rows[2])
            self.var_attend_dep.set(rows[3])
            self.var_attend_time.set(rows[4])
            self.var_attend_date.set(rows[5])
            self.var_attend_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")

if __name__ == "__main__":
    root = Tk()
    app = AttendanceRecord(root)
    root.mainloop()
