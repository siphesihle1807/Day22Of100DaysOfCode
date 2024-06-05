from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Siphe's Ping Pong :) ")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_on = True
while game_on:
    time.sleep(ball.pace)
    screen.update()
    ball.move()


#     Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
#         Collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
#         When ball misses the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_score_increase()


    # when ball misses the l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_score_increase()

#         ending the game



screen.exitonclick()