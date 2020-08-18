from tkinter import *
root = Tk()
e = Entry(root, width=50, bd=5)
e.pack()
e.insert(0, "Enter your name")

def myClick():
    myLabel = Label(root, text="Hello " + e.get())
    myLabel.pack()

myButton = Button(root, text = 'Click here', padx = 50, pady = 50, bd=5,command=myClick)
myButton.pack()

root.mainloop()
