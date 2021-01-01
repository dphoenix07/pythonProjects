from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# Turtle that crosses the road
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.color("black")
        self.setheading(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() >= FINISH_LINE_Y
