import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.create_car()

    def create_car(self):
        while len(self.cars) <= 10:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(1, 2, 1)
            car.setheading(180)
            car.goto(random.randint(-250, 270), random.randint(-250, 270))
            for x in range(1, len(self.cars)):
                while self.cars[x].distance(self.cars[x - 1]) <= 20:
                    car.goto(random.randint(-270, 270), random.randint(-230, 270))
            car.setheading(180)
            self.cars.append(car)

    def moves(self):
        for x in range(0, len(self.cars)):
            self.cars[x].forward(10)
            if self.cars[x].xcor() < -300:
                self.cars[x].color(random.choice(COLORS))
                self.cars[x].goto(300, random.randint(-230, 270))

