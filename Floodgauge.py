from tkinter import *
import ttkbootstrap as tb

root = tb.Window(themename="superhero")
root.title("TTK Boostrap! Floodgauge")
root.geometry("500x350")

def starter():
    my_gauge.start()

def stoper():
    my_gauge.stop()

def incrementer():
    my_gauge.step(10)
    my_label.config(text=f"Position: {my_gauge.variable.get()}")


my_gauge = tb.Floodgauge(root, bootstyle="success",
    font=("Helvetica",18),
    mask="Pos: {}%",
    maximum=80,
    orient="horizontal",
    value=0,
    mode="determinate")
my_gauge.pack(pady=50, fill=X, padx=20)

start_button = tb.Button(root, text="Start", bootstyle="danger outline", command=starter)
start_button.pack(pady=20)

end_button = tb.Button(root, text="End", bootstyle="danger outline", command=stoper)
end_button.pack(pady=20)

inc_button = tb.Button(root, text="Incrementer", bootstyle="danger outline", command=incrementer)
inc_button.pack(pady=20)

my_label = tb.Label(root, text="position: ")
my_label.pack(pady=20)

root.mainloop()