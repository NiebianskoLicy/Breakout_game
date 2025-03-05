from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.life = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(230,-290)
        self.write(f"score:{self.score}", align="center", font=("Courier", 20, "normal"))
        self.goto(350,-290)
        self.write(f"❤{self.life}", align="center", font=("Courier", 20, "normal"))

    def score_point(self):
        self.score += 1
        self.update_scoreboard()

    def lose_life(self):
        self.life -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 40, "normal"))