from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


root = tb.Window(title="TTK bootstrap", themename="superhero")
root.geometry("500x350")

label1 = tb.Label(root, text="Label 1")
label1.pack(pady=40)

separator = tb.Separator(root, bootstyle='danger', orient='horizontal')
separator.pack(fill='x',padx=100)

label2 = tb.Label(root, text="Label 2")
label2.pack(pady=40)

# sizegrip
my_sizegrip = tb.Sizegrip(root, bootstyle='infor')
my_sizegrip.pack(anchor='se', fill='both', expand=True)


root.mainloop()