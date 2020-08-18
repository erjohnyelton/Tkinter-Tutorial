from tkinter import *
root = Tk()

# create a label createWidgets
myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="My is Johny")
myLabel3 = Label(root, text="   ")
#Displaying onto the screen
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()
