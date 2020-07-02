from tkinter import *

def buttonClick(self):
    print('You clicked me !')

def name():
    print('Hello')
root = Tk()
root.title('Welcome to GUI!!!!')
f = Frame(root, height=300, width=700)
f.propagate(0)          # Will not let the frame shrink
f.pack(side=LEFT, anchor="nw")

# 1 WAY
b1 = Button(f, text="Click me", width=15, height=2, bg="yellow", fg='blue', activebackground='red', activeforeground='pink')
b1.pack()
b1.bind("<Button-1>", buttonClick)

# 2 WAY
b2 = Button(f, text="My button", width=15, height=2, bg="yellow", fg='blue', activebackground='red', activeforeground='pink', command=name)
b2.pack(side=LEFT)

root.mainloop()