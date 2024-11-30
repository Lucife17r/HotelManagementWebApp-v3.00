
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk


# Create the main window
top = Tk()
top.title('welcome')
top.geometry('1200x600')

def insert():
    k=e2.get()
    k2=e3.get()
    k3=int(e4.get())
    k4=int(e5.get())
    k5=e6.get()
    k6=e7.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='mysql123',db='Hotel_management')
    cur=db.cursor()
    d="insert into emp values('%s','%s','%s','%s','%s','%s')"%(k,k2,k3,k4,k5,k6)
    result=cur.execute(d)
    if (result>0):
        messagebox.showinfo("Result", "Record insert successfully")

    else:
        messagebox.showinfo("Result", "Record not insert successfully")

    db.commit()

    e2.delete(0, 'end')
    e3.delete(0, 'end')
    e4.delete(0, 'end')
    e5.delete(0, 'end')
    e6.delete(0, 'end')
    e7.delete(0, 'end')


def delete():
    k=e2.get()
    import pymysql as sql
    db =sql.connect(host='localhost',user='root',password='mysql123',db='Hotel_management')
    cur=db.cursor()
    d="delete from emp where name=%s"
    result= cur.execute(d,(k,))


    if result > 0:
        messagebox.showinfo("Result", "Record deleted successfully")

    else:
        messagebox.showinfo("Result", "Record not deleted")

    db.commit()

def search():
    k=e2.get()
    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='mysql123',db='Hotel_management')
    cur=db.cursor()
    d="select * from emp where name=%s"
    cur.execute(d,k)
    result=cur.fetchall()
    for row in result:
        name=row[0]
        password=row[1]
        age=row[2]
        contact=row[3]
        address=row[4]
        email=row[5]
        print(name,password,contact,age,address,email)

def show():

    import pymysql as sql
    db=sql.connect(host='localhost',user='root',password='mysql123',db='Hotel_management')
    cur=db.cursor()
    d="select * from emp"
    cur.execute(d)
    result=cur.fetchall()
    for row in result:
        name=row[0]
        password=row[1]
        age=row[2]
        contact=row[3]
        address=row[4]
        email=row[5]
        tv.insert("",'end', values=(name,password,contact,address,email))


path=r"C:\Users\pc\Downloads\wallpaperflare.com_wallpaper.jpg"
img=ImageTk.PhotoImage(Image.open(path))

L11=Label(top,image=img)
L11.pack()

tv = ttk.Treeview(top)
tv['columns']=('Name', 'password','contact','address','email')
tv.column('#0', width=0, stretch=NO)
tv.column('Name', anchor=CENTER, width=70)
tv.column('password', anchor=CENTER, width=70)
tv.column('contact', anchor=CENTER, width=70)
tv.column('address', anchor=CENTER, width=70)
tv.column('email', anchor=CENTER, width=70)



tv.heading('Name', text='Name', anchor=CENTER)
tv.heading('password', text='password', anchor=CENTER)
tv.heading('contact', text='contact', anchor=CENTER)
tv.heading('address', text='address', anchor=CENTER)
tv.heading('email', text='email', anchor=CENTER)
tv.place(x=920,y=120)



# Title label
L = Label(top, text='Registration', bg='green', fg='white', font=('Arial', 30, 'bold'))
L.place(x=500, y=50)

# Name Label and Entry
L2 = Label(top, text='Name',fg='white',bg='black', font=('Arial', 20, 'bold'))
L2.place(x=300, y=120)
e2 = Entry(top, font=('Arial', 20, 'bold'), width=25)
e2.place(x=450, y=120)

# Password Label and Entry
L3 = Label(top, text='Password', bg='black', fg='white', font=('Arial', 20, 'bold'))
L3.place(x=300, y=180)
e3 = Entry(top, font=('Arial', 20, 'bold'), show='*', width=25)  # Hide password
e3.place(x=450, y=180)

# Age Label and Entry
L4 = Label(top, text='Age', bg='Black', fg='white', font=('Arial', 20, 'bold'))
L4.place(x=300, y=240)
e4 = Entry(top, font=('Arial', 20, 'bold'), width=25)
e4.place(x=450, y=240)

# Contact Label and Entry
L5 = Label(top, text='Contact', bg='black', fg='white', font=('Arial', 20, 'bold'))
L5.place(x=300, y=300)
e5 = Entry(top, font=('Arial', 20, 'bold'), width=25)
e5.place(x=450, y=300)

# Address Label and Entry
L6 = Label(top, text='Address', bg='black', fg='white', font=('Arial', 20, 'bold'))
L6.place(x=300, y=360)
e6 = Entry(top, font=('Arial', 20, 'bold'), width=25)
e6.place(x=450, y=360)

# Email Label and Entry
L7 = Label(top, text='Email', bg='black', fg='white', font=('Arial', 20, 'bold'))
L7.place(x=300, y=420)
e7 = Entry(top, font=('Arial', 20, 'bold'), width=25)
e7.place(x=450, y=420)

# Add button
b1 = Button(top, text='Submit', font=('Arial', 20, 'bold'),command=insert)
b1.place(x=450, y=480)  # Set a specific y-coordinate

b2=Button(top,text='Delete',font=('Arial',20,'bold'),command=delete)
b2.place(x=600, y=480)

b2=Button(top,text='search',font=('Arial',20,'bold'),command=search)
b2.place(x=750, y=480)

b2=Button(top,text='show',font=('Arial',20,'bold'),command=show)
b2.place(x=900, y=480)


# Configure the window background color
top.config(bg='green')

# Start the main loop
top.mainloop()
