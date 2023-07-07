from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.random_position = 0
        self.make_car()

    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6 or random_chance == 3:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            random_position = random.randint(-250, 250)
            car.penup()
            car.goto(x=300, y=random_position)
            car.color(random.choice(COLORS))
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:

            # Check if the car has completed its distance
            if car.xcor() < -300:
                car.color("white")
                self.all_cars.remove(car)

            car.forward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT
