from turtle import *


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.dx = 1.05
        self.dy = 1.05

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1

    def reset_x(self, sign):
        if sign == '+':
            self.setx(390)
        else:
            self.setx(-390)

    def reset_y(self, sign):
        if sign == '+':
            self.sety(290)
        else:
            self.sety(-290)

    def check_collision_wall(self):
        # Border Checking
        if self.xcor() > 390:
            self.reset_x(sign='+')
            self.bounce_x()

        if self.xcor() < -390:
            self.reset_x(sign='-')
            self.bounce_x()

        if self.ycor() > 290:
            self.reset_y(sign='+')
            self.bounce_y()

        if self.ycor() < -290:
            self.reset_y(sign='-')
            self.bounce_y()

    def check_collision_paddle(self, paddle):
        if (self.ycor() < -240) and (paddle.xcor() + 80 > self.xcor() > paddle.xcor() - 80):
            self.sety(-240)
            self.dy *= -1

    def check_game_over(self):
        if self.ycor() < -280:
            print(self.ycor())
            return True
        else:
            return False
