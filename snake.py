from turtle import Turtle, Screen
import time

MOVE_DISTANCE = 20
SNAKE_POSITIONS = [(0,0), (-20,0), (-40,0)]

class Snake:

    def __init__(self) -> None:

        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in SNAKE_POSITIONS:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(i)
            self.segment.append(new_segment)

    def snake_move(self):
        for seg_num in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def left(self):
        self.head.setheading(0)

    def right(self):
        self.head.setheading(180)

    def down(self):
        self.head.setheading(270)
















# if __name__ == "__main__":
#     screen = Screen()
#     screen.setup(width=600, height=600)
#     screen.bgcolor("black")
#     screen.title("My snake game")
#     screen.tracer(0)

#     snake = Snake()

#     for i in SNAKE_POSITIONS:
#         new_segment = Turtle("square")
#         new_segment.penup()
#         new_segment.color("white")
#         new_segment.goto(i)
#         snake.segment.append(new_segment)

#     for _ in range(10):
#         time.sleep(1)
#         screen.update()
#         snake.snake_move()

#     screen.exitonclick()
