import tkinter as tk
from tkinter import ttk
win=tk.Tk()
win.title("Working with combo boxes")

#adding a label
aLabel=ttk.Label(win,text="Combo boxes")
aLabel.grid(column=0,row=0)

def clickMe():
	action.configure(text=" Hello " + name.get() + ' ' + numberChosen.get())

#changing the label
ttk.Label(win,text="Enter a name: ").grid(column=0,row=0)

#adding a name from the Entry widget
name=tk.StringVar()
nameEntered=ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=0,row=1)

#adding a button
action=ttk.Button(win,text="Clicke Me!",command=clickMe)
action.grid(column=2,row=1)

ttk.Label(win, text="Choose a number: ").grid(column=1,row=0)
number=tk.StringVar()
numberChosen=ttk.Combobox(win,width=12,textvariable=number,state='readonly') #adding a readonly state to the combo box making it not write able
numberChosen['values']=(range(50))
numberChosen.grid(column=1,row=1)
numberChosen.current(0)


win.mainloop()


