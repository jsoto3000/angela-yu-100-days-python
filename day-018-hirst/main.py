# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list =  [(228, 227, 226), (246, 237, 243), (243, 244, 246), (234, 166, 59), (45, 112, 157), (113, 150, 203), (212, 123, 164), (16, 128, 96), (172, 44, 88), (1, 177, 143), (153, 18, 54), (224, 201, 117), (225, 76, 115), (163, 166, 35), (28, 35, 84), (227, 86, 43), (42, 166, 208), (120, 172, 116), (119, 102, 158), (215, 64, 33), (237, 244, 241), (39, 52, 100), (76, 21, 45), (229, 169, 188), (14, 99, 71), (31, 61, 56), (8, 92, 107), (222, 177, 169), (181, 188, 208), (171, 203, 193)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
