from tkinter import *

def motion(event):
  print("Mouse position: (%s %s)" % (event.x, event.y))
  return
def click(event):
  print('Click')

def double_click(event):
  print("double Click")

def button2(event):
  print('button2')

def button3(event):
  print('button3')

def button4(event):
  print('button4')

def button5(event):
  print('button5')



master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))
msg.bind('<B3-Motion>',motion)
msg.bind('<Button-1>',click)
msg.bind('<Double-1>',double_click)

msg.bind('<Enter>',button2)
msg.bind('<Leave>',button3)
msg.bind('<FocusIn>',button4)
msg.bind('<FocusOut>',button5)


msg.pack()
mainloop()