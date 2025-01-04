from turtle import Turtle
class Ball:
    def __init__(self):
        self.ball = Turtle(shape="circle")
        self.ball.penup()
        self.ball.color("white")
        self.x_move = 10
        self.y_move = 10
    def move(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)
    def bounce_y(self):
        self.y_move *= -1
    def bounce_x(self):
        self.x_move *= -1

