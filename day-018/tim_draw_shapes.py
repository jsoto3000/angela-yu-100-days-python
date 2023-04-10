########### Challenge 3 - Draw Shapes ########

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon,
# nonagon, and decagon
# Three sided shape to ten sided shape
# Derive angle of each shape by dividing 360 by the corresponding number of sides

import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

# use range 3 thru 11 to include 10
for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)


screen = t.Screen()
screen.exitonclick()