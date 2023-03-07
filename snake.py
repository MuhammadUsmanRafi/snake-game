import random
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
COLOR = ["red", "green", "orange", "blue", "white", "pink", "yellow"]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle(shape="circle")
        segment.width = 20
        segment.penup()
        segment.color(random.choice(COLOR))
        segment.goto(position)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segments in range(len(self.segments) - 1, 0, -1):
            x_pos = self.segments[segments - 1].xcor()
            y_pos = self.segments[segments - 1].ycor()
            self.segments[segments].goto(x_pos, y_pos)
        self.head.forward(MOVE_DISTANCE)

    def Up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def Down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def Left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def Right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)