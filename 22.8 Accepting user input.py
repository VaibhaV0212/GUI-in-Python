from tkinter import *
root = Tk()

def hello():
    print('Submitting form')
    print(f"{namevalue.get(), phonevalue.get(),gendervalue.get(),emergencyvalue.get(), paymentvalue.get(), foodservicevalue.get()}")

    with open("records.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(),gendervalue.get(),emergencyvalue.get(), paymentvalue.get(), foodservicevalue.get()}\n")



root.geometry("644x333")

# Heading
Label(root, text="Welcome to travel", font="comicsansms 13 bold").grid(row=0, column=1)

# Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency contact")
payment = Label(root, text="Payment mode")

# Pack text
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment.grid(row=5, column=2)

# Tkinter variable for storing entries
namevalue= StringVar()
phonevalue= StringVar()
gendervalue= StringVar()
emergencyvalue= StringVar()
paymentvalue= StringVar()
foodservicevalue =StringVar()

# Entries for our form
nameentry = Entry(root, textvariable= namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymententry = Entry(root, textvariable=paymentvalue)

# Packing our entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymententry.grid(row=5, column=3)

# Checkbox and Packing it
foodservice = Checkbutton(text="Want to pre book", variable=foodservicevalue)
foodservice.grid(row=6, column=3)

# Button and Packing it
Button(text="Submit", command=hello).grid(row=7, column=3)

root.mainloop()