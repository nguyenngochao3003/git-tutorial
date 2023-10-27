from tkinter import *
import random

BOARD_WIDTH = 1000
BOARD_HEIGHT = 700
SPACE_SIZE = 50
GANTT_COLOR = "#00FF00"
BACKGROUND_COLOR = 'white'

class gantt():
    def __init__(self):
        # x = 0
        # y = 0
        width = 50
        height = 10
        name = "job 1"
        data = ([10,20],)
        for gant in data:
            print(gant)
            for x, y in gant:
                self.gantt = canvas.create_rectangle(x, y, x + width, y + height, fill='green', tags='gantt')

def move():
    pass



Window = Tk()
Window.title("Schedule gantt")
Window.resizable(False, False)

label = Label(Window, text="Manufacturing Schedule", font=('Arial', 20, 'bold')).pack(pady=5)
canvas = Canvas(Window, bg=BACKGROUND_COLOR, height=BOARD_HEIGHT, width=BOARD_WIDTH)
canvas.pack()

Window.update()

Window_width = Window.winfo_width()
Window_height = Window.winfo_height()
screen_width = Window.winfo_screenwidth()
screen_height = Window.winfo_screenheight()

x = int(screen_width/2-Window_width/2)
y = int(screen_height/2- Window_height/2)
Window.geometry(f"{Window_width}x{Window_height}+{x}+{y}")

label = gantt()


Window.mainloop()