from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()

        self.shape("turtle")

        self.color("blue")
        self.move_up()
        self.setheading(90)
        # self.left(90)
        self.move_speed = 0.1
        self.goto(STARTING_POSITION)
        self.move_to_start()

    def move_up(self):
        # new_y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), new_y)
        self.forward(MOVE_DISTANCE)

    def move_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

