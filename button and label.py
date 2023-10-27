from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb


root = tb.Window(themename="superhero")
# root = tk()
root.title("ttk Bootstrap!")
root.geometry("500x350")


# create a function for the button
counter = 0
def changer():
    global counter
    counter +=1
    if counter %2 ==0:
        my_label.config(text="Hello World")
    else:
        my_label.config(text="Good Bye World")
# color
# Default, primary, secondary, SUCCESS, INFO, Warning, DANGER, LIGHT, DARK


# create a Label
my_label = tb.Label(text="hello world", font=("Helvetica", 28), bootstyle='default, inverse')
my_label.pack(pady=50)


# create Button
my_button = tb.Button(text= 'click me!', bootstyle="success, outline", command=changer)
my_button.pack(pady=20)
root.mainloop()