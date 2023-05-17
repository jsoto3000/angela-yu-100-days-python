import turtle


bat_image = "mini_batman_running.gif"


# add shape to the shape list
turtle.addshape(bat_image)


# check the updated shape list
print(turtle.getshapes())


turtle.shape(bat_image)
turtle.penup()
turtle.setpos(-10, 10)



for i in range(22):
    turtle.fd(40 + 5 * i)
    turtle.right(90)

screen.exitonclick()