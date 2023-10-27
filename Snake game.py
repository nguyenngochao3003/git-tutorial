from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PART = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"
class Snake:
    def __init__(self):
        self.body_size = BODY_PART
        self.coordinates = []    # ghi lại vị trí của các body-part của snake để khi di chuyển nếu cắn đuôi thì game over
        self.squares = []       # để sử dụng cho delete canvas square ở đuôi rắn theo từng key

        for i in range(0, BODY_PART):
            self.coordinates.append([0, 0])
            

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tags='snake')
            self.squares.append(square)

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x,y,x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag='food')


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

    snake.coordinates.insert(0, (x,y))

    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)


    if x == food.coordinates[0] and y == food.coordinates[1]: 

        global score

        score +=1

        label.config(text='Score: {}'.format(score))

        canvas.delete('food')

        food = Food()
    else:
        del snake.coordinates[-1]  # ghi lại vị trí của các body-part của snake để khi di chuyển nếu cắn đuôi thì game over

        canvas.delete(snake.squares[-1])
        
        del snake.squares[-1]   # để sử dụng cho delete canvas square theo từng key

    if check_collisions(snake):
        game_over()
    else:
        Window.after(SPEED, next_turn, snake, food ) 


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

def check_collisions(snake):
    
    print(snake.coordinates)
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print('game over')
            return True

def game_over():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas', 70), text='GAME OVER', fill='red', tag='game over')


Window = Tk()
Window.title("snake game")
Window.resizable(False, False)

score = 0
direction = 'down'

label = Label(Window, text="Score: {} ".format(score), font=('consolas', 40))
label.pack()

canvas = Canvas(Window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

Window.update()

Window_width = Window.winfo_width()
Window_height = Window.winfo_height()
screen_width = Window.winfo_screenwidth()
screen_height = Window.winfo_screenheight()

x = int(screen_width/2-Window_width/2)
y = int(screen_height/2- Window_height/2)
Window.geometry(f"{Window_width}x{Window_height}+{x}+{y}")

Window.bind('<Left>', lambda event: change_direction('left'))
Window.bind('<Right>', lambda event: change_direction('right'))
Window.bind('<Up>', lambda event: change_direction('up'))
Window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()

food = Food()
next_turn(snake=snake, food=food)
Window.mainloop()