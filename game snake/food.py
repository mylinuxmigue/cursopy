from mimetypes import init
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('red')
        self.refresh()
        

    def refresh(self):
        random_x = random.randint(-290,290)
        random_y = random.randint(-290,290)
        self.goto(random_x,random_y)