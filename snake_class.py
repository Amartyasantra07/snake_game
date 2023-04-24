from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in starting_positions:
            snake_part = Turtle("square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(position)
            self.segment.append(snake_part)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)
    #  for seg in segment:
    #     seg.forward(20)

    # snake_part_2 = Turtle("square")
    # snake_part_2.color("white")
    # snake_part_2.goto(-20, 0)

    # snake_part_3 = Turtle("square")
    # snake_part_3.color("white")
    # snake_part_3.goto(-40, 0)
