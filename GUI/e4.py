from hmac import new
from turtle import *
import random

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title='Make your bet',prompt='Wich turtles will win race?')

colors = ['red','orange','blue','yellow','green','purple']
y_position = [-70,-40,-10,20,50,80]


all_turtles = []

for index in range(6):
    new_turtle = Turtle()
    new_turtle.shape('turtle')
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[index])
    all_turtles.append(new_turtle)
    for spin in range(2):
        new_turtle.right(360)
    
if user_bet:
    is_race_on = True
else:
    print('make a bet')
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"you've won! The {winning_turtle} is the winner")
            else:
                print('You have lost')
        turtle.forward(random.randint(1,10))



screen.exitonclick()