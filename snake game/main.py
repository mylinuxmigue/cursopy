from turtle import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
snake = Snake()
food = Food()
turtle = Turtle()
scoreboard = Scoreboard()

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

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #detect when happen a collision with food
    if snake.head.distance(food) < 20:
        scoreboard.increase_score()
        food.refresh()
        snake.extend()

    #detect when happen a collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.GameOver()
        game_is_on = False

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.GameOver()
            game_is_on = False
 
screen.mainloop()