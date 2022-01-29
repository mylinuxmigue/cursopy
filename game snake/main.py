from turtle import *
from snake import Snake
from food import Food
import time

screen = Screen()
snake = Snake()
food = Food()

screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)


#lets code the methods to be able to move our snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

while True:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.mainloop()