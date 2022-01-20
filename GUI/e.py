from turtle import Screen, Turtle


timmy = Turtle()
screen = Screen()


for _ in range(11):
    timmy.forward(20)
    timmy.penup()
    timmy.forward(20)
    timmy.pendown()

screen.exitonclick()