from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


root = tb.Window(title="TTK bootstrap", themename="superhero")
root.geometry("500x350")

def scale(e):
    my_label.config(text=f'{int(my_scale.get())}%')



# Create a scale / slider
my_scale = tb.Scale(root, bootstyle='warning',
    length=400,
    orient='horizontal',
    from_=0,
    to=100,
    command=scale,
    state='normal')
my_scale.pack(pady=30)

#create a label
my_label = tb.Label(root, text="")
my_label.pack()
root.mainloop()