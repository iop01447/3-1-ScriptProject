
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
win = Tk ()
win.title("Raspberry Pi UI")
win.geometry('200x100+200+200')
def clickMe():
        messagebox.showinfo("Button Clicked", str.get())
str = StringVar()
combo = ttk.Combobox(win, width=20, textvariable=str)
combo['values'] = ('apple', 'banana', 'pineapple' , 'pear')
combo.grid(column = 0 , row = 0)
combo.current(0)
action=ttk.Button(win, text="Click Me", command=clickMe)
action.grid(column=0, row=1)
win.mainloop()
