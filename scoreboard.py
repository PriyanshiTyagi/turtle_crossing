from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 0
        self.score()

    def score(self):
        self.write(arg=f"LEVEL= {self.level}", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align='center', font=FONT)

    def level_up(self):
        self.clear()
        self.level += 1
        self.score()
