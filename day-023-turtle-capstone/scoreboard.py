from turtle import Turtle

FONT = ("Comic Sans MS", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-250, 250)
        # self.write("Level: " + str(self.player_score), align="left", font=(FONT))
        self.write(f"Level: {self.level}", align="left", font=FONT)


    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=FONT)
