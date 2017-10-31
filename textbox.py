import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("Textbox GUI")
#adding a labele to the window
aLabel=ttk.Label(win,text="A Lable")
aLabel.grid(column=0,row=0)

def clickMe():
	action.configure(text='Hello ' + name.get())

#changing the label
ttk.Label(win,text="Enter a name: ").grid(column=0,row=0)

#adding a textbox Entry widget
name=tk.StringVar()
nameEntered=ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=0,row=1)

#adding a button
action=ttk.Button(win,text="Click me!",command=clickMe)
action.grid(column=1,row=1)

win.mainloop()
