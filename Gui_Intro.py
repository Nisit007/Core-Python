# First import package
from tkinter import *
import tkinter

# Define Package as Tk
window = tkinter.Tk()

# Change the title of app
window.title("My app")

# Change the window size
window.geometry('1280x720')

# Create a label and placed in window
lbl = Label(window, text="Click here",fg='red',bg='black',font='italic 10 bold')
lbl.place(x = 10, y = 10)

# Create a Button and placed in window
btn = Button(window, text="Click me" ,fg='red', bg='black')
btn.place(x = 50, y = 50)

# Create a Textarea and placed in window
entry = Entry(window, font='bold 10')
entry.place(x = 150,y = 10)

window.mainloop()
