from tkinter import *

from tkcalendar import Calendar,DateEntry

root =Tk()

root.geometry("400x500")
def show():
    s=cal.get()
    print(s)
cal=DateEntry(root,width=30,bg='darkblue',fg='white',year=2010)

b1=Button(root,text='submit',command=show)
b1.place(x=100,y=200)

cal.grid()
root.mainloop()