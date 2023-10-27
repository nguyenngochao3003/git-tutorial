from tkinter import *
import ttkbootstrap as tb

root = tb.Window(title="TTK bootstrap", themename="superhero")
root.geometry("500x350")

def stuff(x):
    my_menu.config(bootstyle=x)
    my_label.config(text=x)

my_menu = tb.Menubutton(root, bootstyle='warning', text='thing!')
my_menu.pack(pady=40)

# Create basic menu
inside_menu = tb.Menu(my_menu)

# Add item to our inside menu
item_var = StringVar()
for x in ['primary', 'secondary', 'danger', 'infor', 'outline primary', 'outline secondary', 'outline danger', 'outline infor']:
    inside_menu.add_radiobutton(label=x, variable=item_var, command=lambda x=x: stuff(x))

# Associate the inside menu with menubutton
my_menu['menu'] = inside_menu

# Crate a label
my_label = tb.Label(root, text="")
my_label.pack(pady=40)


root.mainloop()
