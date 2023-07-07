from turtle import *
import random

UPPER_XCOR = 400
LOWER_XCOR = -400
UPPER_YCOR = 240
LOWER_YCOR = 140


class Block:
    def __init__(self):
        self.random_ylength = [3, 4, 5]
        self.random_block_color = ['light blue', 'royal blue',
                                   'light steel blue', 'steel blue',
                                   'light cyan', 'light sky blue',
                                   'violet', 'salmon', 'tomato',
                                   'sandy brown', 'purple', 'deep pink',
                                   'medium sea green', 'khaki']
        self.all_blocks = []
        self.x_y_position = []
        self.random_stretch_len = []
        self.can_make_more = True

    def make_block(self):
        block = Turtle()
        random_strechlen = random.choice(self.random_ylength)
        self.random_stretch_len.append(random_strechlen)
        block.shapesize(stretch_wid=1, stretch_len=random_strechlen)
        block.shape("square")
        block.color(random.choice(self.random_block_color))
        block.penup()
        self.place_block(block)
        self.all_blocks.append(block)

    def place_block(self, block):
        if len(self.all_blocks) == 0:
            x = UPPER_XCOR - ((self.random_stretch_len[-1] * 20) // 2)
            y = UPPER_YCOR
            self.x_y_position.append((x, y))
            block.goto(x=x, y=y)
        else:
            x = ((self.x_y_position[-1][0] - ((self.random_stretch_len[-2] * 20) // 2)) - (
                    (self.random_stretch_len[-1] * 20) // 2))
            lim = (UPPER_XCOR - ((self.random_stretch_len[-1] * 20) // 2)) * -1
            if x < lim:
                x = UPPER_XCOR - ((self.random_stretch_len[-1] * 20) // 2)
                y = (self.x_y_position[-1][1] - 20)
                if y > LOWER_YCOR:
                    self.x_y_position.append((x, y))
                    block.goto(x=x, y=y)
                else:
                    self.can_make_more = False
                    return
            else:
                y = self.x_y_position[-1][1]
                self.x_y_position.append((x, y))
                block.goto(x=x, y=y)

    def make_all_blocks(self):
        while self.can_make_more:
            self.make_block()
            if not self.can_make_more:
                self.all_blocks[-1].hideturtle()

    def check_collision_ball(self, ball, scoreboard):
        for block in self.all_blocks:
            if block.distance(ball) < 35:
                scoreboard.increase_score()
                self.all_blocks.remove(block)
                block.hideturtle()
                ball.dy *= -1
                return True
        return False
