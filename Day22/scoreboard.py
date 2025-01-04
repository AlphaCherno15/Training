from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(f'Score: Left {self.left_score}/ Right {self.right_score}', align="center", font=("Arial", 24, "normal"))
    def r_scored(self):
        self.right_score += 1
        self.clear()
        self.write(f'Score: Left {self.left_score}/ Right {self.right_score}', align="center", font=("Arial", 24, "normal"))
    def l_scored(self):
        self.left_score += 1
        self.clear()
        self.write(f'Score: Left {self.left_score}/ Right {self.right_score}', align="center", font=("Arial", 24, "normal"))
    def game_over(self):
        self.home()
        self.write(f'You Died', align="center", font=("Arial", 24, "normal"))