from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


root = tb.Window(title="TTK bootstrap", themename="superhero")
root.geometry("500x350")

my_frame = tb.Frame(root)
my_frame.pack(pady=20)

my_scroll = tb.Scrollbar(my_frame, orient='vertical', bootstyle='danger round')
my_scroll.pack(side='right', fill='y')

my_text = Text(my_frame, width=30, height=25, yscrollcommand=my_scroll.set, wrap='none', font=('Helvertica', 18))
my_text.pack()

my_scroll.config(command=my_text.yview)
root.mainloop()