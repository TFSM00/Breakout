from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from brick import BrickManager
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height = 900, width = 700)
screen.bgcolor("black")
screen.title("Atari Breakout")
screen.tracer(0)

def game():
    for turtle in screen.turtles():
        turtle.reset()

    paddle = Paddle(screen)
    ball = Ball(screen)
    brickmanager = BrickManager(screen)
    with open("highscore.txt", 'r', encoding='utf-8') as file:
        highscore = int(file.readlines()[0].strip())

    scoreboard = Scoreboard(screen, brickmanager, highscore)
    FPS = 20
    screen.update()

    screen.listen()
    screen.onkey(paddle.move_left, "Left")
    screen.onkey(paddle.move_right, "Right")
    screen.onkey(paddle.move_left, "a")
    screen.onkey(paddle.move_right, "d")
    screen.onkey(None,'r')
    screen.onkey(None, 'c')

    game_ongoing = True

    def collision(ball, brick):
        return abs(ball.xcor() - brick.xcor()) < 35 and abs(ball.ycor() - brick.ycor()) < 15


    while game_ongoing:
        time.sleep(1/FPS)
        screen.update()

        # Left and Right Wall Collision
        if ball.xcor() > (screen.window_width()/2 - ball.width * 2) \
            or \
           ball.xcor() < (-screen.window_width()/2 + ball.width * 2):
            ball.setheading(180 - ball.heading())

        if ball.ycor() > 0.8 * screen.window_height()/2:
            ball.reset_position()

        if ball.ycor() < - 0.9 * screen.window_height()/2:
            break

        if collision(ball, paddle):
            ball.bounce()

        # Detect collision with brick
        brickmanager.update_available_for_collision()
        if brickmanager.available_for_collision == 0:
            brickmanager.place_bricks()

        for brick in brickmanager.available_for_collision:
            if collision(ball, brick):
                brick.setpos(screen.window_width()*2, 0)
                ball.bounce()
                pos = brickmanager.check_brick_pos(brick)
                del brickmanager.grid[pos[0]][pos[1]]
                brickmanager.score += brick.points
                scoreboard.update_scoreboard()

        ball.move(FPS)

    score = brickmanager.score
    if score > highscore:
        highscore = score
        with open("highscore.txt", "w", encoding='utf-8') as file:
            file.write(str(highscore))

    for turtle in screen.turtles():
        turtle.reset()

    gameover = Turtle(shape='square')
    gameover.shapesize(stretch_wid=5, stretch_len=3)
    gameover.color('white')
    screen.onkey(game,'r')
    screen.onkey(screen.bye, 'c')
    
    gameover.setheading(270)
    gameover.write('Game Over', align='center', font=('Consolas', '30'))
    gameover.forward(40)
    gameover.write(f"Score: {score}", align='center', font=('Consolas', '30'))
    gameover.forward(40)
    gameover.write(f"High Score: {highscore}", align='center', font=('Consolas', '30'))
    gameover.forward(40)
    gameover.write("Press 'R' to Retry", align='center', font=('Consolas', '30'))
    gameover.forward(40)
    gameover.write("Press 'C' to Exit", align='center', font=('Consolas', '30'))
   
    screen.mainloop()

game()
