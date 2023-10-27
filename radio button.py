from tkinter import *
import ttkbootstrap as tb
from datetime import date
from ttkbootstrap.dialogs import Querybox

root = tb.Window(title="TTK bootstrap! Date Entry", themename="superhero")
root.geometry("500x350")
def clicker():
    my_label.config(text=f'You selected: {my_topping.get()}')

#create Radio button list
toppings = ['Pepperoni', 'Cheese', 'Veggie']

# Create A thinkter variable to keep track of everything
my_topping = StringVar()

for topping in toppings:
    tb.Radiobutton(root, bootstyle='danger', variable=my_topping, text=topping, value= topping, command=clicker).pack(pady=20)

# Create button
my_button = tb.Button(root, text="CLICK ME!", command=clicker)
my_button.pack(pady=20)

my_label =  tb.Label(root, bootstyle='infor')
my_label.pack(pady=20)

rb1 = tb.Radiobutton(root, bootstyle='infor toolbutton', variable=my_topping, text='Radio button1', value="Radio button 1", command=clicker)
rb1.pack(pady=20)
rb2 = tb.Radiobutton(root, bootstyle='infor toolbutton outline', variable=my_topping, text='Radio button2', value="Radio button sdfsdf", command=clicker)
rb2.pack(pady=20)

root.mainloop()
