import turtle
import pandas as pd
data = pd.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# def get_mouse_click_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_cor)
us_states_list = data["state"].to_list()
us_states = data["state"]
states_guessed = []
def check_answer():
    global game
    state = (data[us_states == answer_state])
    if answer_state in us_states_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state.x.item(), state.y.item())
        t.write(state.state.item())
        states_guessed.append(state.state.item())
        game += 1
    else:
        print("this is not an state")

game = 0
while game < 50:
    answer_state = screen.textinput(title=f'Guess the State {game}/50',
                                    prompt="What's another state's Name?").title()
    if answer_state == "Exit":
        break
    check_answer()

to_learn = [each for each in us_states if each not in states_guessed]
# for each in us_states:
#     if each not in states_guessed:
#         to_learn.append(each)
new_df = pd.DataFrame(to_learn)
new_df.to_csv("states_to_learn.csv")




turtle.mainloop()