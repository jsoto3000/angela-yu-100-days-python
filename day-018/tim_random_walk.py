########### Challenge 4 - Random Walk ########

# https://en.wikipedia.org/wiki/Random_walk

import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270, 360]
# or tim.pensize(15)
tim.width(15)
tim.speed("fastest")

for i in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()