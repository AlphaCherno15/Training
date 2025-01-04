from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score:{self.high_score}', align="center", font=("Arial", 24, "normal"))
    def scored(self):
        self.score += 1
        self.update_scoreboard()
    def game_over(self):
        self.home()
        self.write(f'You Died', align="center", font=("Arial", 24, "normal"))
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()