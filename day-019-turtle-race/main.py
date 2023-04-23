# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# some slight modification from the original solution
# will revisit for handling tie-breaker

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Turtle Races")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
# y_positions = [-70, -40, -10, 20, 50, 80]
y_positions = [-160, -100, -40, 20, 80, 140]
all_turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-390, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 350:
            is_race_on = False
            winning_color = turtle.pencolor()
            # print(winning_color)
            if winning_color == user_bet:
                turtle.write(f"YOU WIN! The {winning_color} turtle is the winner!", False, align="right", font=('Arial', 10, 'normal'))
                turtle.ht()
            else:
                # print(f"You've lost! The {winning_color} turtle is the winner!")
                turtle.write(f"YOU LOSE! The {winning_color} turtle is the winner!", False, align="right", font=('Arial', 10, 'normal'))
                turtle.ht()
        else:
        #Make each turtle move a random amount.
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

screen.exitonclick()
