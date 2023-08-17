from turtle import Screen
from player import Player
from ball import Ball
from score import Score
import time

my_screen = Screen()
my_screen.setup(width = 800, height = 600)
my_screen.bgcolor("black")
my_screen.title("Pong")
my_screen.listen()
my_screen.tracer(0)

r_paddle = Player(350)
l_paddle = Player(-350)
my_screen.onkey(r_paddle.up, "Up")
my_screen.onkey(r_paddle.down, "Down")
my_screen.onkey(l_paddle.up, "w")
my_screen.onkey(l_paddle.down, "s")

ball = Ball()

r_score = Score(270)
l_score = Score(-270)

ball_speed = 0.1
current_speed = ball_speed
is_on = True

while is_on:
    my_screen.update()
    ball.move()
    time.sleep(current_speed)

#detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    
    if r_paddle.distance(ball) <= 50 and ball.xcor() > 330 or l_paddle.distance(ball) <= 50 and ball.xcor() < -330:
        ball.paddle_bounce()
        current_speed *= 0.8
    
    if ball.xcor() > 380:
        ball.setpos(0,0)
        current_speed = ball_speed
        l_score.add_score()
    
    if ball.xcor() < -380:
        ball.setpos(0,0)
        current_speed = ball_speed
        r_score.add_score()




my_screen.exitonclick()