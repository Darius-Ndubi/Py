import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
win=tk.Tk()
win.title("More on widgets")

#creating a label
aLabel=ttk.Label(win,text="Welcome")
aLabel.grid(column=0,row=0)

def clickMe():
	action.configure(text="Hey " + name.get() + ' ' +numberChosen.get())

#renameing the label above
ttk.Label(win,text="Enter your name: ").grid(column=0,row=0)

#adding a text from the Entry widget
name=tk.StringVar()
nameEntered=ttk.Entry(win,width=12,textvariable=name)
nameEntered.grid(column=0,row=1)
nameEntered.focus()

#adding a button
action=ttk.Button(win,text="Click Me!",command=clickMe)
action.grid(column=2,row=1)

#adding a combo box
#first we create a label for the combo box
ttk.Label(win, text="Choose a number: ").grid(column=1,row=0)
number=tk.StringVar()
numberChosen=ttk.Combobox(win,width=12,textvariable=number)
numberChosen['values']=(range(50))
numberChosen.grid(column=1,row=1)
numberChosen.current(0)

#creating check buttons
chVarDis=tk.IntVar()
check1=tk.Checkbutton(win,text="Disabled",variable=chVarDis,state='disabled')
check1.select()
check1.grid(column=0,row=4,sticky=tk.W)

chVarUn=tk.IntVar()
check2=tk.Checkbutton(win,text="UnChecked",variable=chVarUn)
check2.deselect()
check2.grid(column=1,row=4,sticky=tk.W)

chVarEn=tk.IntVar()
check3=tk.Checkbutton(win,text="Enabled",variable=chVarEn)
check3.select()
check3.grid(column=2,row=4,sticky=tk.W)

#adding radio buttons
#radio button globals
COLOR1="Blue"
COLOR2="Green"
COLOR3="Red"

#radio butoon callback
def radCall():
	radsel=radvar.get()
	if radsel==1: win.configure(background=COLOR1)
	elif radsel==2: win.configure(background=COLOR2)
	elif radsel==3: win.configure(background=COLOR3)

#creating 3 radio buttons using a single variable
radvar=tk.IntVar()
rad1=tk.Radiobutton(win,text=COLOR1,variable=radvar,value=1,command=radCall)
rad1.grid(column=0,row=5,sticky=tk.W,columnspan=3)

rad2=tk.Radiobutton(win,text=COLOR2,variable=radvar,value=2,command=radCall)
rad2.grid(column=1,row=5,sticky=tk.W,columnspan=3)

rad3=tk.Radiobutton(win,text=COLOR3,variable=radvar,value=3,command=radCall)
rad3.grid(column=2,row=5,sticky=tk.W,columnspan=3)

#adding a scroll text widget
#define the width
scrolW=30
#define the height
scrolH=3
scr=scrolledtext.ScrolledText(win, width=scrolW,height=scrolH,wrap=tk.WORD)
scr.grid(column=0,columnspan=3)


win.mainloop()

