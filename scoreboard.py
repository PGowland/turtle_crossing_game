from turtle import Turtle

CAR_SPEED = 0.1


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.goto(-220, 260)
        self.color("black")
        self.write(f"Level = {self.level}", font=("arial", 20, "bold"), align="center")

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level = {self.level}", font=("arial", 20, "bold"), align="center")

    def game_over(self):
        self.clear()
        self.home()
        self.write("GAME OVER!", font=("arial", 60, "bold"), align="center")
        self.goto(0, -100)
        self.write(f"Your final level was: {self.level}", font=("arial", 20, "bold"), align="center")
