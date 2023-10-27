from tkinter import *
import ttkbootstrap as tb

root = tb.Window(title="TTK bootstrap", themename="superhero")
root.geometry("500x350")


#style
my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=('Helvetica',18))
my_button = tb.Button(text="Hello world", 
    bootstyle='success',
    style='success.Outline.TButton',
    width=20)
my_button.pack(pady=40)

root.mainloop()