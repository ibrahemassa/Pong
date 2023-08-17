from turtle import Turtle

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.color("White")
        self.current = 0
        self.setpos(position,225)
        self.write(f"{self.current}", align="center", font = ("Arial", 50, "normal"))
        self.ht()
    
    def add_score(self):
        self.current += 1
        self.clear()
        self.write(f"{self.current}", align="center", font = ("Arial", 50, "normal"))