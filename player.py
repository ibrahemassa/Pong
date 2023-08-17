from turtle import Turtle

class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.setpos(position,0)

    def up(self):
        self.setpos(self.xcor(), self.ycor() + 25)
    
    def down(self):
        self.setpos(self.xcor(), self.ycor() - 25)