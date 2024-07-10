import tkinter
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import numpy as np
import os
import mysql.connector


class Train:
    def __init__(self, root):
        self.root = root
        self.root.title("Train")

        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size and position
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")

        title_lbl = Label(self.root, text="Train Data Set", font=("times new roman", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1400, height=50)

        # background Image
        img_bg = Image.open("images\\developer.jpg")
        img_bg = img_bg.resize((1400, 700))
        self.Photoimg_bg = ImageTk.PhotoImage(img_bg)

        f_lbl = Label(self.root, image=self.Photoimg_bg)
        f_lbl.place(x=0, y=50, width=1400, height=700)

        # Button Image Train Data
        img = Image.open("images\\th.jpeg")
        img = img.resize((200, 200))
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl1 = Label(self.root, image=self.photoimg)
        f_lbl1.place(x=600, y=260, width=200, height=200)
        b2 = tkinter.Button(self.root, image=self.photoimg, cursor="hand2", command=self.train_classifier)
        b2.place(x=600, y=260, width=200, height=200)

        # Button
        b1_1 = tkinter.Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
                              font=("times new roman", 15, "bold"), bg="red", fg="white")
        b1_1.place(x=600, y=460, width=200, height=40)

        dep_Label = tkinter.Label(self.root,
                                  text="Ready to enhance your data or image? Just click the button to start training!",
                                  font=("times new roman", 20, "bold"), fg="red",
                                  bg="white")
        dep_Label.place(x=230, y=600)

    def train_classifier(self):
        data_dir = "data_set"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"Directory '{data_dir}' does not exist.")
            return

        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir) if file.endswith(('.jpg', '.png'))]

        if not path:
            messagebox.showerror("Error", "No images found in the directory.")
            return

        faces = []
        ids = []

        for image in path:
            try:
                img = Image.open(image).convert('L')
                imageNp = np.array(img, 'uint8')
                id = int(os.path.split(image)[1].split('.')[1])
                faces.append(imageNp)
                ids.append(id)
                cv2.imshow("Training", imageNp)
                cv2.waitKey(1)
            except Exception as e:
                print(f"Error processing image {image}: {e}")

        ids = np.array(ids)

        if len(faces) == 0 or len(ids) == 0:
            messagebox.showerror("Error", "No valid training data found.")
            return

        # Train classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training dataset completed!!!")


if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()
