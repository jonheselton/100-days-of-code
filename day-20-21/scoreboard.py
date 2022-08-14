from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        self.highscore = 0

    def get_highscore(self):
        with open('highscore', 'r') as f:
            self.get_highscore = f.read()
    
    def sav_highscore(self):
        with open('highscore', 'w') as f:
            f.seek(0)
            f.write(self.highscore)
            f.truncate()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        if self.score > self.highscore:
            self.highscore = self.score
        self.sav_highscore()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
