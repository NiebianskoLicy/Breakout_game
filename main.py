from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from wall import Wall
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

# main paddle
m_paddle = Paddle((0,-270))
ball = Ball()
scoreboard = Scoreboard()
wall = Wall()

screen.listen()
screen.onkey(m_paddle.go_left,"a")
screen.onkey(m_paddle.go_right,"d")


game_on = True
while game_on:
    time.sleep(0.002)
    screen.update()
    ball.move()

    #Detecting game over
    if scoreboard.life == 0:
        game_on = False
        scoreboard.game_over()

    # Detect collision with walls
    if ball.ycor() > 280:
        ball.y_bounce()
    elif ball.xcor() > 380 or ball.xcor() < -380:
        ball.x_bounce()

    #Detect collision with paddle
    if ball.distance(m_paddle) < 80 and ball.ycor() > -280 or wall.hit(ball):
        ball.y_bounce()
        if wall.hit(ball):
            scoreboard.score_point()


    #Criteria for losing life
    if ball.ycor() < -400:
        ball.reset_position()
        scoreboard.lose_life()

# TODO 1 - fix scoring

screen.exitonclick()