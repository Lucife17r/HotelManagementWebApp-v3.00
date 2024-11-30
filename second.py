
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk



# Create the main window
top=Tk()
top.title('welcome')
top.geometry('1500x700')

def login():
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='mysql123',db='Hotel_management')
    cur=db.cursor()
    cur.execute("select * from emp where name=%s and password=%s",(e2.get(),e3.get()))
    row=cur.fetchone()


    if row == None:
        messagebox.showinfo("Error)", "Invalid username and password")

    else:
        top.destroy()
        import third


path=r"C:\Users\pc\Downloads\wallpaperflare.com_wallpaper.jpg"
img=ImageTk.PhotoImage(Image.open(path))

L11=Label(top,image=img)
L11.pack()





# Title label
L = Label(top, text='Login', bg='green', fg='white', font=('Arial', 30, 'bold'))
L.place(x=500, y=50)

# Name Label and Entry
L2 = Label(top, text='Name', bg='green', fg='white', font=('Arial', 20, 'bold'))
L2.place(x=300, y=120)
e2 = Entry(top, font=('Arial', 20, 'bold'), width=30)
e2.place(x=450, y=120)

# Password Label and Entry
L3 = Label(top, text='Password', bg='green', fg='white', font=('Arial', 20, 'bold'))
L3.place(x=300, y=180)
e3 = Entry(top, font=('Arial', 20, 'bold'), show='*', width=30)  # Hide password
e3.place(x=450, y=180)


# Add button
b4 = Button(top, text='Login', font=('Arial', 20, 'bold'),command=login)
b4.place(x=300, y=250)  # Set a specific y-coordinate


# Start the main loop
top.mainloop()
