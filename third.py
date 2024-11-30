
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkinter import ttk
top=Tk()
# Create the main window
top.title("welcome")
top.geometry('1200x600')

f1=Frame(top,height=300,width=1500,bg='green')
f1.place(x=0,y=0)

f2=Frame(top,height=300,width=1500,bg='Red')
f2.place(x=0,y=300)

e1=Entry(f1)
e1.place(x=200,y=200)




# Add button
b1 = Button(f2,text='submit', font=('Arial', 20, 'bold'))
b1.place(x=100, y=100)  # Set a specific y-coordinate

l=Label(f1,text="Registration",font=('Arial', 30,'bold'))
l.place(x=600,y=10)

k=['select','python','china','meena','veena','reena','seema']

n=ttk.Combobox(f2,values=k)
n.place(x=400,y=200)
n.current(0)

c1=Checkbutton(f1,text='python')
c1.place(x=800,y=70)
c1=Checkbutton(f1,text='java')
c1.place(x=800,y=100)
c1=Checkbutton(f1,text='python')
c1.place(x=800,y=130)

r1=Radiobutton(f2,text='male',value=1)
r1.place(x=800,y=200)
r2=Radiobutton(f2,text='female',value=2)
r2.place(x=900,y=200)
r3=Radiobutton(f2,text='other',value=3)
r3.place(x=1000,y=200)

r1.select()


# Configure the window background color


# Start the main loop
top.mainloop()
