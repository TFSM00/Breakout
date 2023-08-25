from turtle import Turtle

UP = 90
DOWN = 270
TURTLE_WIDTH = 20
PADDLE_MOVE_SIZE = 40
BALL_MOVE_SIZE = 10

class Brick(Turtle):
    def __init__(self, color, points):
        super().__init__()
        self.shape("square")
        self.brick_color = color
        self.color(self.brick_color)
        self.width = TURTLE_WIDTH * 3
        self.height = TURTLE_WIDTH
        self.shapesize(stretch_wid = self.height/TURTLE_WIDTH, stretch_len = self.width/TURTLE_WIDTH)
        self.penup()
        self.points = points
        
class BrickManager():
    def __init__(self, window) -> None:
        self.width = TURTLE_WIDTH * 3
        self.height = TURTLE_WIDTH
        self.window = window
        self.colors = {'yellow': 1, 'green': 3, 'orange': 5, 'red': 7}
        self.gap = 10
        self.grid = None
        self.max_brick = self.max_bricks()
        self.available_for_collision = None
        self.place_bricks()
        self.score = 0

    def max_bricks(self):
        brick_num = int(self.window.window_width()/(TURTLE_WIDTH * 3))
        gap_size = self.gap * (brick_num - 1)
        total_size = brick_num * (TURTLE_WIDTH * 3) + gap_size
        if total_size > self.window.window_width():
            return brick_num - 1
        return brick_num
    
    def place_bricks(self):
        current_x = - self.window.window_width()/2 + self.width/2
        current_y = 0.2 * self.window.window_height()/2
        self.grid = []
        for color, points in list(self.colors.items()):
            for _ in range(2):
                row = []
                for _ in range(self.max_brick):
                    brick = Brick(color, points)
                    brick.setpos(current_x, current_y)
                    current_x += self.width + self.gap
                    row.append(brick)
                # Reset x position and go up on y position
                self.grid.append(row)
                current_x = - self.window.window_width()/2 + self.width/2
                current_y += self.height + self.gap

    def flat_grid(self, grid):
        return [brick for row in grid for brick in row]

    def update_available_for_collision(self):
        self.available_for_collision = [self.grid[0]]
        for index, row in enumerate(self.grid):
            if len(row) < self.max_brick:
                try:
                    self.available_for_collision.append(self.grid[index + 1])
                except IndexError:
                    pass
        
        self.available_for_collision = self.flat_grid(self.available_for_collision)
    
    def check_brick_pos(self, brick):
        return [(i, row.index(brick)) for i, row in enumerate(self.grid) if brick in row][0]
                

        

