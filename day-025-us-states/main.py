import turtle
import pandas

screen = turtle.Screen()
screen.title("United States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# how to get x, y coordinates for stated on image
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    # note: use title case method to make answer upper/lower case insensitive
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # print(answer_state)

    # enter "exit" in prompt to generate new file with states not guessed
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(answer_state)
        t.write(state_data.state.item())

screen.exitonclick()