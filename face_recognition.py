import tkinter as tk
from idlelib import tree
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import csv
import os
from datetime import datetime
import shutil
import cv2
import mysql.connector

class FaceRecognitionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size and position
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Load and display title image
        img_bg = Image.open("images\\developer.jpg")
        img_bg = img_bg.resize((1400, 700))
        self.Photoimg_bg = ImageTk.PhotoImage(img_bg)
        f_lbl = Label(self.root, image=self.Photoimg_bg)
        f_lbl.place(x=0, y=50, width=1400, height=700)

        # Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        # Button for Face Recognition
        b1_1 = Button(self.root, text="Face Recognition", command=self.face_recog, cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=500, y=300, width=300, height=40)

        # Label for information
        dep_Label = Label(self.root,
                          text="Register your attendance effortlessly by clicking the face recognition button!",
                          font=("times new roman", 20, "bold"), fg="red",
                          bg="white")
        dep_Label.place(x=240, y=600)

        # Create buttons for each day of the week
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.attendance_status = {}
        for i, day in enumerate(days_of_week):
            btn = Button(self.root, text=day, command=lambda d=day: self.set_attendance_day(d), cursor="hand2",
                         font=("times new roman", 15, "bold"), bg="blue", fg="white")
            btn.place(x=100, y=200 + i * 50, width=200, height=40)

        # Generate Report Button
        report_btn = Button(self.root, text="Generate Attendance Report", command=self.generate_report_gui, cursor="hand2",
                            font=("times new roman", 15, "bold"), bg="green", fg="white")
        report_btn.place(x=500, y=350, width=300, height=40)

        # Display All Attendance Records Button
        display_attendance_btn = Button(self.root, text="Display All Attendance", command=self.display_all_attendance, cursor="hand2",
                                        font=("times new roman", 15, "bold"), bg="orange", fg="white")
        display_attendance_btn.place(x=500, y=400, width=300, height=40)

    def set_attendance_day(self, day):
        self.attendance_status["current_day"] = day
        print(f"Current attendance day set to: {day}")
        self.face_recog()

    def mark_attendance(self, student_id, name, roll, department, status):
        attendance_file_path = os.path.abspath("attendance_reports/attendance.csv")
        now = datetime.now()
        dateString = now.strftime("%Y-%m-%d")
        current_day = self.attendance_status.get("current_day", "Unknown")

        with open(attendance_file_path, "a+", newline="") as file:
            file.seek(0)
            reader = csv.reader(file)
            rows = list(reader)
            header = ["Student ID", "Name", "Roll No", "Department", "Time", "Date", "Attendance Status"] + \
                     ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

            # Write the header only if the file is empty
            if len(rows) == 0:
                writer = csv.writer(file)
                writer.writerow(header)

            # Check if the student has already been marked present for today
            for row in rows:
                if row[0] == str(student_id) and row[6] == "Present" and row[5] == dateString:
                    print("Attendance already marked for:", name)
                    return

            dtString = now.strftime("%H:%M:%S")
            row = [student_id, name, roll, department, dtString, dateString, status]
            attendance_record = {day: ("Present" if day == current_day else "") for day in header[7:]}

            writer = csv.writer(file)
            writer.writerow(row + list(attendance_record.values()))
            print(f"Attendance marked for: {name} on {current_day} as {status}")

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            coord = []
            student_info = {}

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(host="localhost", user="root", password="03493674002", database="fyp")
                my_cursor = conn.cursor()

                my_cursor.execute("SELECT Name FROM student_data WHERE Student_id = %s", (id,))
                n = my_cursor.fetchone()
                if n is not None:
                    n = n[0]
                else:
                    n = "Unknown"

                my_cursor.execute("SELECT Roll FROM student_data WHERE Student_id = %s", (id,))
                r = my_cursor.fetchone()
                if r is not None:
                    r = r[0]
                else:
                    r = "Unknown"

                my_cursor.execute("SELECT Dep FROM student_data WHERE Student_id = %s", (id,))
                d = my_cursor.fetchone()
                if d is not None:
                    d = d[0]
                else:
                    d = "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Roll: {r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep: {d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    student_info = {"id": id, "name": n, "roll": r, "dep": d}
                    self.mark_attendance(id, n, r, d, "Present")  # Mark attendance as present
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(id, n, r, d, "Absent")  # Mark attendance as absent

                coord = [x, y, w, h]

                # Print debug information
                print(f"ID: {id}, Name: {n}, Roll: {r}, Department: {d}, Confidence: {confidence}%")

            return coord, student_info

        def recognize(img, clf, faceCascade):
            coord, student_info = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img, student_info

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break
            img, student_info = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            key = cv2.waitKey(1)
            if key == ord('p'):  # 'p' key to mark attendance
                if student_info:
                    self.mark_attendance(student_info['id'], student_info['name'], student_info['roll'],
                                         student_info['dep'], "Present")
            elif key == 13:  # Enter key to break
                break

        video_cap.release()
        cv2.destroyAllWindows()

    def generate_report(self) -> object:
        attendance_file_path = os.path.abspath("attendance_reports/attendance.csv")
        report_file_path = os.path.abspath("attendance_reports/attendance_report.csv")

        with open(attendance_file_path, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)

            if len(rows) < 2:
                print("No attendance data available to generate report.",parent=self.root)
                return

            header = rows[0]
            data = rows[1:]

            student_attendance = {}

            for row in data:
                student_id = row[0]
                if student_id not in student_attendance:
                    student_attendance[student_id] = {"Name": row[1], "Roll No": row[2], "Department": row[3], "Days Present": 0, "Total Days": 0, "Days Absent": 0}

                for day in header[7:]:
                    if row[header.index(day)] == "Present":
                        student_attendance[student_id]["Days Present"] += 1
                    elif row[header.index(day)] == "Absent":
                        student_attendance[student_id]["Days Absent"] += 1

                student_attendance[student_id]["Total Days"] += 1

            with open(report_file_path, "w", newline="") as report_file:
                writer = csv.writer(report_file)
                report_header = ["Student ID", "Name", "Roll No", "Department", "Days Present", "Days Absent", "Total Days", "Attendance Percentage"]
                writer.writerow(report_header)

                for student_id, attendance_data in student_attendance.items():
                    days_present = attendance_data["Days Present"]
                    days_absent = attendance_data["Days Absent"]
                    total_days = attendance_data["Total Days"]
                    attendance_percentage = (days_present / total_days) * 100 if total_days > 0 else 0
                    writer.writerow([student_id, attendance_data["Name"], attendance_data["Roll No"], attendance_data["Department"], days_present, days_absent, total_days, f"{attendance_percentage:.2f}%"])

            print(f"Attendance report generated at: {report_file_path}")

    def generate_report_gui(self):
        # Generate the attendance report
        self.generate_report()

        # Open a new tkinter window to display the report
        report_window = Toplevel(self.root)
        report_window.title("Weekly Attendance Report")
        report_window.geometry("1000x600")

        # Title label
        title_lbl = Label(report_window, text="Weekly Attendance Report", font=("times new roman", 20, "bold"),
                          bg="white", fg="red")
        title_lbl.pack(pady=10)

        # Create a frame for treeview and scrollbar
        frame = Frame(report_window)
        frame.pack(fill=BOTH, expand=True)

        # Create a Treeview widget
        tree = ttk.Treeview(frame, columns=(
            "Student ID", "Name", "Roll No", "Department", "Days Present", "Days Absent", "Total Days",
            "Attendance Percentage"),
                            show="headings")
        tree.pack(fill=BOTH, expand=True)

        # Define columns
        tree.heading("Student ID", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Roll No", text="Roll No")
        tree.heading("Department", text="Department")
        tree.heading("Days Present", text="Days Present")
        tree.heading("Days Absent", text="Days Absent")
        tree.heading("Total Days", text="Total Days")
        tree.heading("Attendance Percentage", text="Attendance Percentage")

        # Configure column weights
        tree.column("Student ID", width=100, anchor=tk.CENTER)
        tree.column("Name", width=150, anchor=tk.CENTER)
        tree.column("Roll No", width=100, anchor=tk.CENTER)
        tree.column("Department", width=150, anchor=tk.CENTER)
        tree.column("Days Present", width=100, anchor=tk.CENTER)
        tree.column("Days Absent", width=100, anchor=tk.CENTER)
        tree.column("Total Days", width=100, anchor=tk.CENTER)
        tree.column("Attendance Percentage", width=150, anchor=tk.CENTER)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.configure(yscrollcommand=scrollbar.set)

        # Read the generated report file and display its contents
        report_file_path = os.path.abspath("attendance_reports/attendance_report.csv")
        with open(report_file_path, "r") as report_file:
            reader = csv.reader(report_file)
            header = next(reader)  # Read the header row

            # Display header
            tree.insert("", "end", values=header, tags=("header",))
            tree.tag_configure("header", background="lightgrey")

            # Display data rows
            for idx, row in enumerate(reader, start=1):
                tree.insert("", "end", iid=idx, values=row)

        # Create a frame for search and export functionality
        btn_frame = Frame(report_window, bg="lightgrey")
        btn_frame.pack(fill=X, padx=10, pady=10)

        # Search Bar and Button
        search_var = StringVar()
        search_entry = Entry(btn_frame, textvariable=search_var, font=("times new roman", 15), bd=3, relief=GROOVE)
        search_entry.pack(side=LEFT, padx=20, pady=10)

        search_button = Button(btn_frame, text="Search",
                               command=lambda: self.search_records(tree, search_var, report_file_path),
                               font=("times new roman", 15, "bold"), bg="blue", fg="white", cursor="hand2")
        search_button.pack(side=LEFT, padx=10, pady=10)

        # Export Button
        export_button = Button(btn_frame, text="Export Report", command=lambda: self.export_report(report_file_path),
                               font=("times new roman", 15, "bold"), bg="green", fg="white", cursor="hand2")
        export_button.pack(side=LEFT, padx=10, pady=10)

    def search_records(self, tree, search_var, report_file_path):
        keyword = search_var.get().strip().lower()
        if keyword == "":
            messagebox.showwarning("Empty Search", "Please enter a Name to search.",parent=self.root)
            return

        # Clear existing data in treeview
        for row in tree.get_children():
            tree.delete(row)

        # Reload data based on search results
        with open(report_file_path, "r") as report_file:
            reader = csv.reader(report_file)
            header = next(reader)  # Read the header row

            # Display header
            tree.insert("", "end", values=header, tags=("header",))
            tree.tag_configure("header", background="lightgrey")

            # Display data rows matching search criteria
            for row in reader:
                if keyword in row[1].lower() or keyword in row[2].lower():
                    tree.insert("", "end", values=row)

    def export_report(self, report_file_path):
        export_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if export_file_path:
            shutil.copyfile(report_file_path, export_file_path)
            messagebox.showinfo("Export Successful", f"Attendance report has been exported to:\n{export_file_path}",parent=self.root)

    def display_all_attendance(self):
        # Open a new tkinter window to display all attendance records
        display_window = Toplevel(self.root)
        display_window.title("All Attendance Records")
        display_window.geometry("1000x600")

        # Title label
        title_lbl = Label(display_window, text="All Attendance Records", font=("times new roman", 20, "bold"),
                          bg="white", fg="red")
        title_lbl.pack(pady=10)

        # Create a frame for treeview and scrollbar
        frame = Frame(display_window)
        frame.pack(fill=BOTH, expand=True)

        # Create a Treeview widget
        tree = ttk.Treeview(frame,
                            columns=("Student ID", "Name", "Roll No", "Department", "Time", "Date", "Attendance Status",
                                     "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"),
                            show="headings")
        tree.pack(fill=BOTH, expand=True)

        # Define columns
        tree.heading("Student ID", text="Student ID")
        tree.heading("Name", text="Name")
        tree.heading("Roll No", text="Roll No")
        tree.heading("Department", text="Department")
        tree.heading("Time", text="Time")
        tree.heading("Date", text="Date")
        tree.heading("Attendance Status", text="Attendance Status")
        tree.heading("Monday", text="Monday")
        tree.heading("Tuesday", text="Tuesday")
        tree.heading("Wednesday", text="Wednesday")
        tree.heading("Thursday", text="Thursday")
        tree.heading("Friday", text="Friday")
        tree.heading("Saturday", text="Saturday")
        tree.heading("Sunday", text="Sunday")

        # Configure column weights
        tree.column("Student ID", width=100, anchor=tk.CENTER)
        tree.column("Name", width=150, anchor=tk.CENTER)
        tree.column("Roll No", width=100, anchor=tk.CENTER)
        tree.column("Department", width=150, anchor=tk.CENTER)
        tree.column("Time", width=100, anchor=tk.CENTER)
        tree.column("Date", width=100, anchor=tk.CENTER)
        tree.column("Attendance Status", width=150, anchor=tk.CENTER)
        tree.column("Monday", width=100, anchor=tk.CENTER)
        tree.column("Tuesday", width=100, anchor=tk.CENTER)
        tree.column("Wednesday", width=100, anchor=tk.CENTER)
        tree.column("Thursday", width=100, anchor=tk.CENTER)
        tree.column("Friday", width=100, anchor=tk.CENTER)
        tree.column("Saturday", width=100, anchor=tk.CENTER)
        tree.column("Sunday", width=100, anchor=tk.CENTER)

        # Add a scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.configure(yscrollcommand=scrollbar.set)

        # Search Bar and Button
        search_var = StringVar()
        search_entry = Entry(display_window, textvariable=search_var, font=("times new roman", 15), bd=3, relief=GROOVE)
        search_entry.pack(side=TOP, padx=20, pady=10, fill=X)

        search_button = Button(display_window, text="Search",
                               command=lambda: self.search_records(tree, search_var, attendance_file_path),
                               font=("times new roman", 15, "bold"), bg="blue", fg="white", cursor="hand2")
        search_button.pack(side=TOP, padx=20, pady=10)

        # Export Button
        export_button = Button(display_window, text="Export", command=lambda: self.export_records(attendance_file_path),
                               font=("times new roman", 15, "bold"), bg="green", fg="white", cursor="hand2")
        export_button.pack(side=BOTTOM, padx=20, pady=10)

        # Load attendance data
        attendance_file_path = os.path.abspath("attendance_reports/attendance.csv")

        with open(attendance_file_path, "r") as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row

            # Display data rows
            for row in reader:
                tree.insert("", "end", values=row)

    def search_records(self, tree, search_var, attendance_file_path):
        keyword = search_var.get().strip().lower()
        if keyword == "":
            messagebox.showwarning("Empty Search", "Please enter a keyword to search.",parent=self.root)
            return

        # Clear existing data in treeview
        for row in tree.get_children():
            tree.delete(row)

        # Reload data based on search results
        with open(attendance_file_path, "r") as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row

            # Display data rows matching search criteria
            for row in reader:
                if any(keyword in field.lower() for field in row):
                    tree.insert("", "end", values=row)

    def export_records(self, attendance_file_path):
        export_file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if export_file_path:
            shutil.copyfile(attendance_file_path, export_file_path)
            messagebox.showinfo("Export Successful", f"Attendance data has been exported to:\n{export_file_path}", parent=self.root)

        # Load attendance data
        attendance_file_path = os.path.abspath("attendance_reports/attendance.csv")

        with open(attendance_file_path, "r") as file:
            reader = csv.reader(file)
            header = next(reader)  # Read the header row

            # Display data rows
            for row in reader:
                tree.insert("", "end", values=row)

    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = FaceRecognitionApp(root)
    app.mainloop()
