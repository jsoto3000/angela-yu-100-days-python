########### Challenge 2 - Draw a Dashed Line ########

import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")

for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

screen = t.Screen()
screen.exitonclick()