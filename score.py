from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open('data.txt', mode='r') as hs:
            self.high_score = int(hs.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()

    def increase_score(self):
        self.current_score += 1
        self.update_scoreboard()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open('data.txt', mode="w") as hs:
                hs.write(f"{self.high_score}")
        self.current_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.current_score} High Score: {self.high_score}", move=False, align="center", font=("Courier", 15, "bold"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align="center", font=("Courier", 15, "bold"))
