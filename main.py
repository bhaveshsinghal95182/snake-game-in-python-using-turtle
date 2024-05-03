from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
snake.create_snake()

screen.update()


game_is_on = True
while game_is_on:
    time.sleep(1)
    screen.update()

    snake.snake_move()
    
    












screen.exitonclick()