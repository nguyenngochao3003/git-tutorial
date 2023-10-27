from tkinter import *
import ttkbootstrap as tb

root = tb.Window(title="TTK bootstrap", themename="superhero")
root.geometry("500x350")

def checker():
    if var1.get() ==1:
        my_label.config(text='Check')
    else:
        my_label.config(text="uncheck!")

# Label
my_label = Label(text="Click the checkbutton below", font=("Helvetica", 18))
my_label.pack(pady=(40, 10))


# Button
var1 = IntVar()
my_check = tb.Checkbutton(bootstyle='primary',
    text="check me out",
    variable=var1,
    onvalue=1,
    offvalue=0,
    command=checker)
my_check.pack(pady=10)

# Toolbutton
var2 = IntVar()
my_check2 = tb.Checkbutton(bootstyle='danger, toolbutton',
    text="ToolButton!",
    variable = var2,
    onvalue = 1,
    offvalue = 0,
    command=checker)
my_check2.pack(pady=10)

# Outlines ToolButton!
var3 = IntVar()
my_check3 = tb.Checkbutton(bootstyle='danger, toolbutton, outline',
    text="Outline ToolButton!",
    variable = var3,
    onvalue = 1,
    offvalue = 0,
    command=checker)
my_check3.pack(pady=10)

# Round toggle Button
var4 = IntVar()
my_check4 = tb.Checkbutton(bootstyle='success, round-toggle',
    text="Round Toggle!",
    variable = var4,
    onvalue = 1,
    offvalue = 0,
    command=checker)
my_check4.pack(pady=10)

# Square toggle button
var5 = IntVar()
my_check5 = tb.Checkbutton(bootstyle='warning, Square-toggle',
    text="Square Toggle!",
    variable = var5,
    onvalue = 1,
    offvalue = 0,
    command=checker)
my_check5.pack(pady=10)


root.mainloop()