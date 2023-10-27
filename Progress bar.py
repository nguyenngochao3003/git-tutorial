from tkinter import *
import ttkbootstrap as tb
from PIL import Image
Image.CUBIC = Image.BICUBIC
import time

root = tb.Window(title="TTK bootstrap! Date Entry", themename="superhero")
root.geometry("500x350")

# increment 20
def increment():
    # my_progress.step(20)
    my_progress['value'] += 20
    # Get current value
    my_label.config(text=my_progress['value'])

def start():
    my_progress.start(10)

def stop():
    my_progress.stop()

def auto():
    for x in range(5):
        my_progress['value']+=20
        my_label.config(text=my_progress['value'])
        # Update one at a time not all at once
        root.update_idletasks()
        time.sleep(1)
# progress bar
my_progress = tb.Progressbar(root, bootstyle= 'danger',
    maximum=100,
    mode='determinate',
    length=300,
    value=20)

my_progress.pack(pady=40)

# Frame
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

# Button
my_button = tb.Button(my_frame, text="increment 20", bootstyle='infor', command=increment)
my_button.grid(column=0, row=0, padx=10)

my_button1 = tb.Button(my_frame, text="start", bootstyle='infor', command=start)
my_button1.grid(column=1, row=0, padx=10)

my_button2 = tb.Button(my_frame, text="stop", bootstyle='infor', command=stop)
my_button2.grid(column=2, row=0, padx=10)

my_button3 = tb.Button(my_frame, text="auto", bootstyle='infor', command=auto)
my_button3.grid(column=3, row=0, padx=10)

# Label
my_label = tb.Label(root, text="")
my_label.pack(pady=20)
root.mainloop()