from tkinter import *
root = Tk()
def myClick():
    myLabel = Label(root, text="Look, I Clicked myButton!")
    myLabel.pack()

myButton = Button(root, text = 'Click here', padx = 50, pady = 50, command=myClick)
myButton.pack()

root.mainloop()
