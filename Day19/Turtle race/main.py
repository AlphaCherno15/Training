from turtle import Turtle, Screen
import random as rd

rob = Turtle()
rob.color("purple")
rob.shape("turtle")
amanda = Turtle()
amanda.color("pink")
amanda.shape("turtle")
irane = Turtle()
irane.color("red")
irane.shape("turtle")
celio = Turtle()
celio.color("blue")
celio.shape("turtle")
nice = Turtle()
nice.color("green")
nice.shape("turtle")

competitors = [rob, amanda, irane, celio, nice]
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make yor bet", "which turtle will win the race? Enter a color: ")

def start_pos(turtle, y):
    turtle.penup()
    # turtle.setx(-200)
    # turtle.sety(y)
    turtle.goto(x=-200, y=y)
def race_pace():
    pace = int(rd.randint(1, 10))
    return pace
def winner():
    pass

y_pos = -100
for competitor in competitors:
    start_pos(competitor, y_pos)
    y_pos += 50

distance = 100
end_race = False
while end_race is False:
    for competitor in competitors:
        if competitor.xcor() > 230:
            winning_color = competitor.pencolor()
            if winning_color == user_bet:
                print(f'You won')
                end_race = True
            else:
                print(f'You Lost, the winner was {winning_color}.')
                end_race = True

        competitor.forward(race_pace())

    distance -= 1

# def forward():
#     rob.forward(10)
# def backwards():
#     rob.backward(10)
# def left():
#     rob.left(10)
# def right():
#     rob.right(10)
# def clear():
#     rob.clear()
#     rob.penup()
#     rob.home()
#     rob.pendown()
# screen.listen()
# screen.onkeypress(key="w", fun=forward)
# screen.onkeypress(key="a", fun=left)
# screen.onkeypress(key="s", fun=backwards)
# screen.onkeypress(key="d", fun=right)
# screen.onkeypress(key="c", fun=clear)

# colors = ["red", "orange", "yellow", "green", "blue",  "purple"]
# y_pos = -100
# for turtles in range(0, 6):
#     thor = Turtle(shape="turtle")
#     thor.penup()
#     thor.color(colors[turtles])
#     start_pos(thor, y_pos)
#     y_pos += 50
screen.exitonclick()