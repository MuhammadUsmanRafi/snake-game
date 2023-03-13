from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.count = 0
        with open("Score_file.txt", "r") as file:
            self.high_Score = int(file.read())
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.increase()

    def increase(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score : {self.count} High_Score : {self.high_Score}", True, "center", ("Arial", 12, "normal"))
        self.count += 1

    def reset(self):
        if self.count > self.high_Score:
            self.high_Score = self.count
            with open("Score_file.txt", "w") as file:
                file.write(f"{self.high_Score}")
        self.count = 0
        self.increase()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", True, "center", ("Arial", 12, "normal"))
