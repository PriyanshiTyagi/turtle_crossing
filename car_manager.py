import turtle as t
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(t.Turtle):
    def __init__(self):
        super().__init__()
        self.speed('slow')
        self.pu()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2)
        self.y=random.randint(-240,250)
        # self.x = random.randint( 300,2000)
        # self.distance = STARTING_MOVE_DISTANCE
        self.goto(300,self.y)

    def move(self):
        self.bk(STARTING_MOVE_DISTANCE)

    @staticmethod
    def speed_inc():
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT




