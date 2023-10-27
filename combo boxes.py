from tkinter import *
import ttkbootstrap as tb

root = tb.Window(title="TTK bootstrap", themename="superhero")
root.geometry("500x350")

my_label = tb.Label(root, text="hello world", font=("Helvetica",18))
my_label.pack(pady=30)

# Create button click function
def clicker():
    my_label.config(text=f"You Clicked on {my_combo.get()}!")

# Create Binding function
def click_bind(e):
    my_label.config(text=f"You Clicked  dfgd on {my_combo.get()}!")

# Create Dropdown Options 
days = ['Monday', 'Tueday', 'Wedneday', 'Thusday', 'Friday', 'Satuday', 'Sunday']

#Create combobox 
my_combo = tb.Combobox(root, bootstyle='success', values=days)
my_combo.pack(pady=20)

#set combo default
my_combo.current(0)

#Create a button 
my_button = tb.Button(root, text="Click me!", command=clicker, bootstyle="danger")
my_button.pack(pady=20)

#Bind the combobox
my_combo.bind('<<ComboboxSelected>>', click_bind)
root.mainloop()