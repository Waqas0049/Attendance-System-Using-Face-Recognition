from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser

class Help:
    def __init__(self, root):
        self.root = root
        self.root.title("Help Desk")


        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size and position
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        # Title Label
        title_lbl = Label(self.root, text="HELP DESK", font=("Helvetica", 35, "bold"), bg="white", fg="red")
        title_lbl.pack(side=TOP, fill=X)

        # Background Image
        img_bg = Image.open(r"C:\Users\Waqas Ahmad\Desktop\images\developer.jpg")
        img_bg = img_bg.resize((1300, 650), )
        self.Photoimg_bg = ImageTk.PhotoImage(img_bg)
        bg_lbl = Label(self.root, image=self.Photoimg_bg)
        bg_lbl.pack(fill=BOTH, expand=True)

        # Contact Info Frame
        info_frame = Frame(bg_lbl, bd=2, bg="white", relief=RIDGE)
        info_frame.place(x=50, y=100, width=1200, height=500)

        contact_info = [
            ("Email:", "waqasuom@gmail.com", "red"),
            ("Contact No:", "03493674002", "green"),
            ("WhatsApp:", "03493674002", "red")
        ]

        for i, (label, info, color) in enumerate(contact_info):
            Label(info_frame, text=label, font=("Helvetica", 25, "bold"), fg=color, bg="white").place(x=50, y=50 + i * 100)
            Label(info_frame, text=info, font=("Helvetica", 25, "bold"), fg=color, bg="white").place(x=300, y=50 + i * 100)

        # Buttons for Email and WhatsApp
        email_button = Button(info_frame, text="Send Email", command=self.send_email, font=("Helvetica", 20, "bold"), bg="#d77337", fg="white", cursor="hand2")
        email_button.place(x=50, y=350, width=220, height=50)

        whatsapp_button = Button(info_frame, text="Send WhatsApp", command=self.send_whatsapp, font=("Helvetica", 20, "bold"), bg="#25D366", fg="white", cursor="hand2")
        whatsapp_button.place(x=300, y=350, width=220, height=50)

    def send_email(self):
        email_address = "waqasuom@gmail.com"
        subject = "Help Request"
        body = "Dear Waqas Ahmad,\n\nI need help with..."
        webbrowser.open(f"mailto:{email_address}?subject={subject}&body={body}")

    def send_whatsapp(self):
        phone_number = "+923493674002"  # Include country code
        message = "Hello, I need help with..."
        url = f"https://api.whatsapp.com/send?phone={phone_number}&text={message}"
        webbrowser.open(url)

if __name__ == "__main__":
    root = Tk()
    app = Help(root)
    root.mainloop()
