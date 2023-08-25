from turtle import Turtle

UP = 90
DOWN = 270
TURTLE_WIDTH = 20
PADDLE_MOVE_SIZE = 40
BALL_MOVE_SIZE = 10

class Paddle(Turtle):
    def __init__(self, window):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.window = window
        self.width = TURTLE_WIDTH * 3 
        self.height = TURTLE_WIDTH
        self.shapesize(stretch_wid = self.height/TURTLE_WIDTH, stretch_len = self.width/TURTLE_WIDTH)

        self.x_pos = 0
        self.y_pos = -0.8 * self.window.window_height()/2
        self.penup()
        self.setpos(self.x_pos, self.y_pos)

    def move_right(self):
        if self.position()[0] + self.width > self.window.window_width()/2:
            pass
        else:
            self.goto(self.position()[0] + PADDLE_MOVE_SIZE, self.position()[1])
    def move_left(self):
        if self.position()[0] - self.width < -self.window.window_width()/2:
           pass
        else:
            self.goto(self.position()[0] - PADDLE_MOVE_SIZE, self.position()[1])    
