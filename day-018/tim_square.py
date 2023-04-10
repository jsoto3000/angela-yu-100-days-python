########### Challenge 1 - Draw a Square ###########


import turtle as t

tim = t.Turtle()
tim.shape("turtle")
tim.color("blue")

for i in range(4):
    tim.forward(100)
    tim.left(90)

screen = t.Screen()
screen.exitonclick()