import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkeypress(key="Up", fun=turtle.go_up)
screen.onkeypress(key="Right", fun=turtle.go_right)
screen.onkeypress(key="Left", fun=turtle.go_left)
screen.onkeypress(key="Down", fun=turtle.go_down)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.make_car()
    car.move_car()

    for curr_car in car.all_cars:

        # Detect the collision
        if curr_car.distance(turtle) <= turtle.distance_from_car:
            score.game_over_message()
            game_is_on = False
            break

    if turtle.xcor() < -280 or turtle.xcor() > 280 or turtle.ycor() < -290:
        game_is_on = False
        score.game_over_message()

    # Increase the level and reset the turtle position
    if turtle.ycor() > 270:
        car.increase_speed()
        turtle.turtle_reset()
        score.update_score()

screen.exitonclick()
