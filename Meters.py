from tkinter import *
import ttkbootstrap as tb
from PIL import Image
Image.CUBIC = Image.BICUBIC

root = tb.Window(title="TTK bootstrap", themename="superhero")
root.geometry("500x650")

global counter 
counter =20
def clicker():
    global counter
    if counter <=100:
        my_meter.configure(amountused=counter)
        counter +=5
        my_button.configure(text=f'Click Me {my_meter.amountusedvar.get()}')
    
def up():
    my_meter.step(10)

def down():
    my_meter.step(-10)
    
my_meter = tb.Meter(root, bootstyle="danger",
    subtext="Tkinter Leaned",
    interactive=True,
    textleft="#",
    # textright="%"
    metertype="full", # can be full, semi
    stripethickness=10,
    metersize=200,
    padding=50,
    amountused=0,
    amounttotal=100,
    subtextstyle="success"
    )

my_button = tb.Button(root, text="Click me 5", command=clicker)
my_button.pack(pady=20)

my_button1 = tb.Button(root, text="up", command=up)
my_button1.pack(pady=20)

my_button2 = tb.Button(root, text="down", command=down)
my_button2.pack(pady=20)

my_meter.pack(pady=30)


root.mainloop()
