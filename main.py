from turtle import Screen
from paddle import Paddle
from ball import Ball
screen = Screen()
screen.screensize(canvwidth=600,canvheight=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

r_padd = Paddle((280,0))
l_padd = Paddle((-280,0))
ball = Ball()

screen.listen()
screen.onkey(r_padd.up,"Up")
screen.onkey(r_padd.down,"Down")
screen.onkey(l_padd.up,"w")
screen.onkey(l_padd.down,"s")



is_game_on=True
while is_game_on:
    screen.update()
    ball.move()



screen.exitonclick()