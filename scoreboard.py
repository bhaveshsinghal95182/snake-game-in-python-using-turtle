from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("snake game\snake-game-in-python-using-turtle\data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def scoreboard_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("snake game\snake-game-in-python-using-turtle\data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
        

    # def game_over(self):
    #     self.goto((0,0))
    #     self.write("GAME OVER", font=FONT, align=ALIGNMENT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()