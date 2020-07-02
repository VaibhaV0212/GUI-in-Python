from tkinter import *

def clicked():
    print(uservalue.get())    # get()- get the value
    print(f"The value of password is {passvalue.get()}")

root = Tk()
root.geometry("655x333")

user = Label(root, text="Username")
password = Label(root, text="password")
user.grid()
password.grid(row=1)

# 4 variable class in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=clicked).grid()

root.mainloop()