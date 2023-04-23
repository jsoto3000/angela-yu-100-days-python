# screen setup
# turning snake body

from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# turn off tracer for animation
screen.tracer(0)

# tuples
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    # delay animation
    time.sleep(0.1)

    # for loop with range including start, stop, and step
    # for seg_num in range(start=2, stop=0, step=-1):
    for seg_num in range(len(segments) - 1, 0, -1):
        # segments 2, 1, 0
        # grab second to last segment
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        # last segment to go to position of second to last position
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
