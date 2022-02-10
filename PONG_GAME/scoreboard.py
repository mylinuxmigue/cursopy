from turtle import Turtle

class Scoreboard(Turtle):
    #INITIAL_POSITION = (0,265)
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.goto((-100,200))
        self.write(self.l_score,'center',font=('Arial',20,'bold'))
        self.goto((100,200))
        self.write(self.r_score,'center', font=('Arial', 20,'bold'))

    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    
