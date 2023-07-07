from turtle import *


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(0, -250)

    def paddle_right(self):
        x = self.xcor()
        x += 20
        self.setx(x)

    def paddle_left(self):
        x = self.xcor()
        x -= 20
        self.setx(x)

    def key_bindings(self, wn):
        wn.listen()
        wn.onkeypress(self.paddle_right, "Right")
        wn.onkeypress(self.paddle_left, "Left")

    def check_collision_wall(self):
        # Paddle and Wall Collisions
        if self.xcor() > 320:
            self.setx(320)

        if self.xcor() < -320:
            self.setx(-320)
