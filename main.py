from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

sleep_time = 0.2

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.increase_score()
        snake.extend_segment()
        food.refresh()
        if sleep_time > 0.05:
            sleep_time -= 0.01

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        sleep_time = 0.2
        score.reset()
        snake.reset()

    for segment in snake.segments[1: len(snake.segments) - 1]:
        if snake.head.distance(segment) < 5:
            sleep_time = 0.2
            score.reset()
            snake.reset()

screen.exitonclick()
