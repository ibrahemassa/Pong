from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.y_move = 10
        self.x_move = 10

    def move(self):
        self.setpos(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        # self.y_move *= -1
        self.x_move *= -1
