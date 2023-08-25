from turtle import Turtle
from random import randint
UP = 90
DOWN = 270
TURTLE_WIDTH = 20
PADDLE_MOVE_SIZE = 20
BALL_MOVE_SIZE = 10

class Ball(Turtle):
    def __init__(self, window):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.width = TURTLE_WIDTH/2
        self.height = TURTLE_WIDTH/2
        self.shapesize(stretch_wid = self.height/TURTLE_WIDTH, stretch_len = self.width/TURTLE_WIDTH)
        self.penup()
        self.window = window
        self.x_pos = 0
        self.y_pos = -0.6 * self.window.window_height()/2
        self.setpos(self.x_pos, self.y_pos)
        self.speed(1)
        self.setheading(randint(20, 160))

    def move(self, fps):
        # Sets heading as the top right corner
        # heading = math.degrees(math.atan(600/800))
        self.forward(200*(fps**(-1)))

    def bounce(self):
        if self.heading() % 180 == 0:
            self.setheading(180)
        else: 
            self.setheading(360 - self.heading())

    def reset_position(self):
        self.goto(self.x_pos, self.y_pos)
        self.setheading(randint(20, 160))
        
