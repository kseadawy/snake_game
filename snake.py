from turtle import Turtle
from turtledemo.penrose import start

DISTANCE = 20
INITIAL_LENGTH = 3
INITIAL_SPEED = 4
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        for i in range(INITIAL_LENGTH):
            self.add_segment((i*-20,0))
        self.head = self.segments[0]
        self.tail = self.segments[-1]

    def add_segment(self, position):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.speed(INITIAL_SPEED)
        seg.setpos(position)
        self.segments.append(seg)

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            next_position = self.segments[i-1].pos()
            self.segments[i].setpos(next_position)
        self.segments[0].forward(DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.add_segment(self.tail.pos())
        self.tail = self.segments[-1]

    def speeder(self):
        cur_speed = self.head.speed()
        for segment in self.segments:
            new_speed = cur_speed+1
            segment.speed(new_speed)
        print(f"new speed is: {new_speed}")