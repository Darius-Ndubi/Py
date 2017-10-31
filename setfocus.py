import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("Working with python GUI")

#Adding a label
aLabel=ttk.Label(win,text="Name")
aLabel.grid(column=0,row=0)

#what happens when the Button is clicked
def clickMe():
	action.configure(text='Hello ' + name.get())

#changing the label
ttk.Label(win,text="Enter a name: ").grid(column=0,row=0)

#adding a textbox Entry widget
name=tk.StringVar()
nameEntered=ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0,row=1)

#adding a Button
action=ttk.Button(win,text="Click Me!", command=clickMe)
action.grid(column=1,row=1)
#disabling a button with
action.configure(state='disable')
nameEntered.focus() #focus the cursor in the textbox

win.mainloop()
