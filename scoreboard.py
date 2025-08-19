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
        self.high_score = int(self.read_high_score())
        self.update_score()


    def reset(self):
        self.score = -1

    def read_high_score(self):
        with open("./data/score.txt") as score_file:
            return score_file.read()

    def write_high_score(self):
        with open("./data/score.txt", "w") as score_file:
            score_file.write(str(self.high_score))

    def adjust_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.write_high_score()
        self.reset()
        self.update_score()

    def update_score(self):
        self.score+=1
        self.setpos(x=0, y=250)
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(x=0, y=0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)