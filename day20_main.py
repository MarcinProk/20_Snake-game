from turtle import Screen
import time
from day20_snake import Snake
from day20_food import Food
from day20_score import Scoreboard

screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)            # po tracer zawsze trzeba użyć update! 

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        # snake.speed_up()
        scoreboard.count_score()

    
    # detect collision with walls
    if (snake.head.xcor() > 290 
        or snake.head.xcor() <-290 
        or snake.head.ycor() > 290 
        or snake.head.ycor() < -290):
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for blocks in snake.snake:
        if blocks == snake.head:
            pass
        elif snake.head.distance(blocks) < 10:
            scoreboard.reset()
            snake.reset()
        
    time.sleep(0.01)

screen.exitonclick()