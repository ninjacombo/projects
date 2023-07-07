from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.level = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(x=-210, y=260)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)

    def update_score(self):
        self.level += 1
        self.write_score()

    def game_over_message(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!", align="center", font=FONT)
