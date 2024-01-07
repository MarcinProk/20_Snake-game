from turtle import Turtle, Screen
import time

# Create snake body
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
STARTING_SPEED = 20
SPEED_INCREASE = 2
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.snake_speed = STARTING_SPEED

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        snake_block = Turtle(shape='square')
        snake_block.penup()
        snake_block.color('white')
        snake_block.goto(position)
        self.snake.append(snake_block)

    def extend(self):
        self.add_block(self.snake[-1].position())

    def move(self):
        for segment in range(len(self.snake)-1, 0, -1):         # od ostatniego segmentu, do zera, przeskok o 1
            new_x = self.snake[segment-1].xcor()
            new_y = self.snake[segment-1].ycor()
            self.snake[segment].goto(new_x,new_y)
        self.head.forward(self.snake_speed)

    def speed_up(self):
        self.snake_speed += SPEED_INCREASE

    def snake_up(self):
        if self.head.heading() != DOWN:     # wąż nie może iść w tył
            self.head.setheading(UP)        # naprowadzam tylko 1 blok, reszta ma follow
    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)    
    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for block in self.snake:
            block.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        self.head.goto(0,0)