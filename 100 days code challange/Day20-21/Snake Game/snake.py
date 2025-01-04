from turtle import Turtle
X_POS = 0
Y_POS = 0
POS = (X_POS, Y_POS)
PACE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    def create_snake(self):
        for snakes in range(0, 3):
            self.add_segment(X_POS)
    def move(self):
            for seg_num in range(len(self.segments) - 1, 0, -1 ):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x, new_y)
            self.head.forward(PACE)
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
    def add_segment(self, position):
        global X_POS
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.goto(POS)
        X_POS += -20
        self.segments.append(snake)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def reset(self):
        for part in self.segments:
            part.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]