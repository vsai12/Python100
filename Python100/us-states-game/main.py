import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def title_prompt(curr_score):
    if curr_score > 0:
        return screen.textinput(title=f"{curr_score}/50 States Correct", prompt="What's another state's name?:").title()
    return screen.textinput(title="Guess the State", prompt="Guess a state's name:").title()


score = 0
correct_guess = []
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
data = pd.read_csv("50_states.csv")
while score < 50:
    answer_state = title_prompt(score)
    if answer_state == "Exit":
        all_states = data["state"].to_list()
        missed = list(set(all_states) - set(correct_guess))
        new_data = pd.DataFrame(missed)
        new_data.to_csv("states_to_learn.csv")
        break
    row = data[data["state"] == answer_state]
    if len(row) == 1:
        score += 1
        correct_guess.append(answer_state)
        new_x = row.iloc[0]["x"]
        new_y = row.iloc[0]["y"]
        position = (new_x, new_y)
        writer.goto(position)
        writer.write(answer_state)


