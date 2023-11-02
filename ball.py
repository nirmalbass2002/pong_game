from turtle import Turtle

class Ball(Turtle):


    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.turtlesize(1,1)
        self.penup()
    def move(self):
        if self.distance()
        new_x = self.xcor()+0.1
        new_y = self.ycor()+0.1
        self.goto(new_x,new_y)
