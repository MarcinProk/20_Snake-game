from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    # 20 x 0,5, wtedy ma 10
        self.color('orange')
        self.speed('fastest')
        self.refresh()
        rand_x = random.randint(-260, 260)
        rand_y = random.randint(-260, 260)
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = random.randint(-260, 260)
        rand_y = random.randint(-260, 260)
        self.goto(rand_x, rand_y)