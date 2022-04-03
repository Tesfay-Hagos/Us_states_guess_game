import turtle
import pandas as pd

screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while 1:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states guessed correctly", prompt="what's another state's name?").title()
    turtle_1 = turtle.Turtle()
    turtle_1.hideturtle()
    turtle_1.penup()
    if answer_state == "Exit":
        missing_states = []
        for lists in all_states:
            if lists not in guessed_states:
                missing_states.append(lists)
                location = data[data["state"] == lists]
                turtle_1.goto(int(location.x), int(location.y))
                turtle_1.write(lists)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    elif answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
            location = data[data["state"]==answer_state]
            turtle_1.goto(int(location.x), int(location.y))
            turtle_1.write(answer_state)











screen.mainloop()
