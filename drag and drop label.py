from tkinter import *
from typing import Any
from ttkbootstrap.constants import *
import ttkbootstrap as tb

class draw():
    def __init__(self, width, height, x, y):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def drag_start(self, event):
        widget =event.widget
        widget.startX = event.x
        widget.startY = event.y
        print("x: ",widget.startX)
        print("y: ",widget.startY)

    def drag_motion(self, event):
        widget =event.widget
        x = widget.winfo_x() - widget.startX + event.x
        y = widget.winfo_y() - widget.startY + event.y
        widget.place(x=x, y=y)

    def draw(self):
        root = Tk()
        label = Label(root, bg="red", width=self.width, height= self.height)
        label.place(x=self.x, y=self.y)

        label.bind("<Button-1>",self.drag_start(Event))
        label.bind("<B1-Motion>",self.drag_motion(Event))   

        root.mainloop()


class OO():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y 

    def plus(self):
        self.z = 1
        return self.z + self.x

a= draw(width=10, height=5, x=5,y=5)
a.draw()