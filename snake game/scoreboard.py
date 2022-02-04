from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto((0,270))
        self.color('white')
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write(f'Score {self.score}',align='center', font= ('Times New Roman', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def GameOver(self):
        self.goto(0,0)
        self.write(f'Game Over {self.score}',align='center', font= ('Times New Roman', 20, 'normal'))
