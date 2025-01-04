
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
scoreboard = Scoreboard()
paddle = Paddle()
ball = Ball()
screen.listen()
screen.onkey(lambda: paddle.up("head"),"Up")
screen.onkey(lambda: paddle.down("head"),"Down")
screen.onkey(lambda: paddle.up("opponent"),"w")
screen.onkey(lambda: paddle.down("opponent"),"s")

game_on = True
while game_on is True:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ball.ycor() > 281 or ball.ball.ycor() < -281:
        ball.bounce_y()
    if ball.ball.distance(paddle.head) < 60 and ball.ball.xcor() > 350 or ball.ball.distance(paddle.opponent) < 40 and ball.ball.xcor() < -350:
        print("here")
        ball.bounce_x()
    if ball.ball.xcor() > 370 or ball.ball.xcor() < -370:
        ball.ball.home()
        scoreboard.l_scored()
    elif ball.ball.xcor() < -370:
        ball.ball.home()
        scoreboard.r_scored()

screen.exitonclick()