from turtle import Turtle

FONT = ("courier", 24, "normal")
ALIGNMENT = "center"
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.hideturtle()
        self.penup()
        self.color("white")
        self.increment_score()


    def increment_score(self):
        self.score+=1
        self.setpos(x=0, y=250)
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(x=0, y=0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)