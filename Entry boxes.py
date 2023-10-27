from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")

# root = tk() 
root.title("TTK Bootstrap! Combobox")
root.geometry("500x350")

# Create Entry function
def speak():
    my_label.config(text=f"You typed: {my_entry.get()}")

# Create entrry Widget
my_entry = tb.Entry(root, bootstyle='success', 
    font=('Helvetica', 18),
    foreground="green",
    width=15,
    show="*")
my_entry.pack(pady=50)


# Create button
my_button = tb.Button(root, bootstyle='danger outline', text='Click Me', command=speak)
my_button.pack(pady=20)

# Create Label
my_label = tb.Label(root, text="")
my_label.pack(pady=20)


root.mainloop()