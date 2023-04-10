# Python Tuples
# my_tuple = (1, 3, 8)
# Similar to list
# my_tuple[0] = 1
# Tuples are immutable
# Cannot be changed once created
# RGB Calculator Tool: https://www.w3schools.com/colors/colors_rgb.asp


########### Challenge 4 - Random Walk ########

# https://en.wikipedia.org/wiki/Random_walk

import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

directions = [0, 90, 180, 270, 360]
# or tim.pensize(15)
tim.width(15)
tim.speed("fastest")

for i in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
