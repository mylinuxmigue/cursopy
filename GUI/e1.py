from turtle import Screen, Turtle


timmy = Turtle()
screen = Screen()

timmy.shape('turtle')

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)



screen.exitonclick()