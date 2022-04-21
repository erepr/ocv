import datetime
import time

from tkinter import *
root = Tk()
def send():
    send=datetime.datetime.now().strftime("%x") + " " + datetime.datetime.now().strftime("%X") + " You => "+e.get()
    txt.insert(END, "\n"+send)
    e.delete(0, END) 
txt = Text(root)
txt.grid(row=0, column=0, columnspan = 2)
e=Entry(root, width=100)
send=Button(root, text="Send", command=send).grid(row=1, column=1)
e.grid(row=1, column=0)
root.title("Chat")
root.mainloop()