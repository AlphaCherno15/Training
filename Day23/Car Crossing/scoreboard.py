from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.write(f'Score: {self.score}', align="Left", font=FONT)
    def level(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align="Left", font=FONT)
    def game_over(self):
        self.home()
        self.write(f'You died', align="Left", font=FONT)