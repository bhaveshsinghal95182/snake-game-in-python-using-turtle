from turtle import Turtle
import time

MOVE_DISTANCE = 20
SNAKE_POSITIONS = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

