from turtle import *
from blocks import Block
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

# Breakout Game

# Screen
wn = Screen()
wn.title("Breakout Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Blocks
block = Block()
block.make_all_blocks()

# Paddle
paddle = Paddle()

# Ball
ball = Ball()

# Scoreboard
scoreboard = Scoreboard()
scoreboard.update_score()

# Keyboard Binding
paddle.key_bindings(wn)

# Main Game Loop
while True:
    wn.update()
    # time.sleep(0.01)

    # Check collision with the blocks
    block.check_collision_ball(ball, scoreboard)

    # Move the ball
    ball.move()

    # Check collision with the wall
    ball.check_collision_wall()

    # Paddle and Ball Collisions
    ball.check_collision_paddle(paddle)

    # Paddle and Wall Collisions
    paddle.check_collision_wall()

    # Check collision with the blocks
    block.check_collision_ball(ball, scoreboard)

    # Check if game is over
    if ball.check_game_over():
        break

# Game Over Text
game_over = Turtle()
game_over.color("white")
game_over.penup()
game_over.hideturtle()
game_over.goto(0, 0)
game_over.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

scoreboard.reset()

wn.exitonclick()
