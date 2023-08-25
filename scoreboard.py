from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, window, brick_manager, highscore):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.window = window
        self.brick_manager = brick_manager
        self.highscore = highscore
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.setpos(0, 0.85 * self.window.window_height()/2)
        self.write(f"Score: {self.brick_manager.score}   High Score: {self.highscore}", 
                   align = "center", font = ("Courier", 30, "normal"))
    
