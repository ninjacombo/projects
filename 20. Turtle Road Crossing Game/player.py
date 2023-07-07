from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.distance_from_car = 33
        self.turtle_reset()

    def turtle_reset(self):
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.distance_from_car *= 0.9

    def go_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        # self.setheading(270)
        self.backward(MOVE_DISTANCE)

    def go_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def go_left(self):
        self.setheading(180)
        self.forward(10)
