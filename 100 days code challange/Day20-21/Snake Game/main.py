from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
game_on = True

while game_on is True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scored()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # scoreboard.game_over()
        # time.sleep(1)
        scoreboard.reset_score()
        snake.reset()
        # game_on = False
    for part in snake.segments[2:]:
        if snake.head.distance(part) < 10:
            # scoreboard.game_over()
            # time.sleep(1)
            scoreboard.reset_score()
            snake.reset()
            # scoreboard.game_over()
            # game_on = False

screen.exitonclick()

# segments = []
# y_pos = 0
# x_pos = 0
# for snakes in range(0, 3):
#     snake = Turtle(shape="square")
#     snake.penup()
#     snake.color("white")
#     snake.goto(x=x_pos, y=y_pos)
#     x_pos += -20
#     segments.append(snake)
# game_on = True
# while game_on is True:
#     screen.update()
#     time.sleep(0.1)
    # for seg_num in range(len(segments) - 1, 0, -1 ):
    #     new_x = segments[seg_num - 1].xcor()
    #     new_y = segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x, new_y)
    # segments[0].forward(20)