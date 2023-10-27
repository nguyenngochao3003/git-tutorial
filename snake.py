from tkinter import *
import random
from typing import Any

GAME_WIDTH = 700
GAME_HEIGHT = 700
BODY_PART = 3
SPACE_SIZE = 50
SPEED = 100
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


class Snake():
    def __init__(self):
        self.body_part = BODY_PART
        self.squares = []
        self.coordinates = []
        
        for i in range(0, self.body_part):
            self.coordinates.append([0,0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags='Snake')
            self.squares.append(square)

class Food():
    def __init__(self):
        x = random.randint(0, GAME_WIDTH / SPACE_SIZE - 1) * SPACE_SIZE
        y = random.randint( 0, GAME_HEIGHT / SPACE_SIZE -1) * SPACE_SIZE
        self.coordinates = [x,y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tags='food')

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE 
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.coordinates.insert(0,[x,y])


    

    window.after(SPEED, next_turn, snake, food)



def change_direction(new_direction):
    global direction

    if new_direction =='left':
        if direction != 'right':
            direction = new_direction
    elif new_direction =='right':
        if direction != 'left':
            direction = new_direction
    elif new_direction =='down':
        if direction != 'up':
            direction = new_direction
    elif new_direction =='up':
        if direction != 'down':
            direction = new_direction     

def check_collisions():
    pass

def game_over():
    pass


window = Tk()
window.title("Snake Game")

score = 0
direction = 'down'

label = Label(window, text="Score: 0", font=('consolas', 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, width=GAME_WIDTH, height=GAME_HEIGHT)
canvas.pack()

window.update()

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window_width = window.winfo_width()
window_height = window.winfo_height()

x = int(screen_width/2-window_width/2)
y = int(screen_height/2 - window_height/2)
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

food = Food()
snake = Snake()

next_turn(snake=snake, food=food)


window.mainloop()