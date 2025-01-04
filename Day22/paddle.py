from turtle import Turtle
X_POS = 350
Y_POS = 0
POS = (X_POS, Y_POS)

class Paddle:
    def __init__(self):
        self.segments = []
        self.create_paddle()
        self.head = self.segments[0]
        self.opponent = self.segments[1]
    def create_paddle(self):
        global X_POS
        for paddles in range(0, 2):
            self.add_segment(X_POS, Y_POS)
            X_POS *= -1
    def up(self, who):
        if who == "head":
            if self.head.ycor() < 243:
                new_y = self.head.ycor() + 20
                self.head.goto(self.head.xcor(), new_y)
        else:
            if self.opponent.ycor() < 243:
                new_y = self.opponent.ycor() + 20
                self.opponent.goto(self.opponent.xcor(), new_y)
    def down(self, who):
        if who == "head":
            if self.head.ycor() > -240:
                new_y = self.head.ycor() - 20
                self.head.goto(self.head.xcor(), new_y)
        else:
            if self.opponent.ycor() > -240:
                new_y = self.opponent.ycor() - 20
                self.opponent.goto(self.opponent.xcor(), new_y)
    def add_segment(self, x, y):
        paddle = Turtle(shape="square")
        paddle.turtlesize(5, 1)
        paddle.penup()
        paddle.color("white")
        paddle.goto(x, y)
        self.segments.append(paddle)
    def enemy_mov(self):
        pass