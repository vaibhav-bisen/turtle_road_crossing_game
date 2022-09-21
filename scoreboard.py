from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 1
        self.score_write()

    def score_write(self):
        self.goto(-200, 260)
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.score_write()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


