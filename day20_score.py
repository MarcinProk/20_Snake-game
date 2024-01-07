from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:\\Users\\marci\\Desktop\\Programowanie\\KURSY\\100_exercise\\exercises\\day20_snake\\data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0,250)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", 
                   align='center', font=('Arial', 20, 'normal'))
        self.hideturtle()

    def count_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", 
                   align='center', font=('Arial', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("C:\\Users\\marci\\Desktop\\Programowanie\\KURSY\\100_exercise\\exercises\\day20_snake\\data.txt", 'w') as data:
                data.write(f'{self.high_score}')

        self.score = 0
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", 
                   align='center', font=('Arial', 20, 'normal'))
