from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.count = 0
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.increase()

    def increase(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score : {self.count}", True, "center", ("Arial", 12, "normal"))
        self.count += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", True, "center", ("Arial", 12, "normal"))
