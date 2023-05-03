# import package
import turtle
import os



curr_dir = os.getcwd()
print(curr_dir)

bat_image = os.path.expanduser(f"{curr_dir}/mini_batman_running.gif")


# add shape to the shape list
turtle.addshape(name=bat_image, shape=None)


# check the updated shape list
print(turtle.getshapes())

turtle.shape(bat_image)
turtle.penup()
turtle.setpos(-10, 10)



for i in range(22):
    turtle.fd(40 + 5 * i)
    turtle.right(90)