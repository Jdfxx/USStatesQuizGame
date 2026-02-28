import pandas as pd
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

map_turtle = Turtle()
map_turtle.shape(image)
map_turtle.penup()

writer = Turtle()
writer.hideturtle()
writer.penup()

# Load data and prepare case-insensitive lookup
data = pd.read_csv("50_states.csv")
all_states = data.state.str.lower().to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                               prompt="What's another state's name?")
    # If user cancels the input dialog, textinput returns None
    if answer is None:
        break

    answer_state = answer.strip().lower()

    if answer_state == "exit":


    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_row = data[data['state'].str.lower() == answer_state].iloc[0]
        x_coord = int(state_row['x'])
        y_coord = int(state_row['y'])
        writer.goto(x_coord, y_coord)
        writer.write(state_row['state'], align="center", font=("Arial", 10, "normal"))


screen.exitonclick()