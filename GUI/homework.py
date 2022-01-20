from turtle import *
import random

line = Turtle()
screen = Screen()

colormode(255)

def random_color():
    r = random.randint(0,255)
    g =random.randint(0,255)
    b = random.randint(0,255)

    random_col = (r,g,b)
    return random_col

def edges(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        line.forward(30)
        line.right(angle)

for v in range(3,10):
    edges(v)
    line.color(random_color())




screen.exitonclick()


