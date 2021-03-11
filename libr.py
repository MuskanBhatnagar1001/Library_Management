import tkinter as tk
from PIL import ImageTk, Image  # PIL -> Pillow
import pymysql
from tkinter import messagebox
from Addbook import *
from ViewBooks import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *


mypass = "bhat@1001" #use your own password
mydatabase="mb" #The database name
con = pymysql.connect (host="localhost", user="root", password=mypass, database=mydatabase)
#root is the username here
cur = con.cursor() #cur -> cursor


root = tk.Tk()
root.title("DIGITAL LIBRARY MANAGEMENT SYSTEM")
root.minsize(width=400, height=400)
root.geometry("600x500")

headingFrame1 = tk.Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = tk.Label(headingFrame1, text="WELCOME TO MIT LIBRARY ", bg='black', fg='white',
                        font=('Courier', 15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = tk.Button(root, text="Add Book Details", bg='black', fg='white', command=addBook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = tk.Button(root, text="Delete Book", bg='black', fg='white', command=delete)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = tk.Button(root, text="View Book List", bg='black', fg='white', command=View)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = tk.Button(root, text="Issue Book to Student", bg='black', fg='white', command=issueBook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = tk.Button(root, text="Return Book", bg='black', fg='white', command=returnBook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

same = True
n = 0.25
# Adding a background image
# background_image = Image.open(rb"C://Users//lenovo//Documents//Library//images//mit.jpg")
# [imageSizeWidth, imageSizeHeight] = background_image.size
# newImageSizeWidth = int(imageSizeWidth*n)
# if same:
#   newImageSizeHeight = int(imageSizeHeight*n)
# else:
#   newImageSizeHeight = int(imageSizeHeight/n)

# background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
# img = ImageTk.PhotoImage(background_image)
# Canvas1 = Tk.Canvas(root)
# Canvas1.create_image(300,340,image = img)
# Canvas1.config(bg="white",width = newImageSizeWidth, height = newImageSizeHeight)
# Canvas1.pack(expand=True,fill=BOTH)

root.mainloop()
