import random
from turtle import Turtle



# Constances
STATRING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

preColors = ["green", "blue", "yellow", "orange", "purple", "ivory", "grey", "pink", "cyan4", "purple1", "red", "LimeGreen", "brown", "DeepSkyBlue"]
def random_color(preColors): # 14
    a = random.randint(0, 13)
    color = preColors[a]
    return color

class Snake():

    def __init__(self):
        self.body_parts = []
        self.create_snake()
        self.head = self.body_parts[0]
    
    def create_snake(self):    
        for position in STATRING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        self.body_parts.append(Turtle("square"))
        self.body_parts[-1].color(random_color(preColors))
        self.body_parts[-1].penup()
        self.body_parts[-1].goto(position)    
    
    
    def extend(self):
        self.add_segment(self.body_parts[-1].position())
       
    def move_body(self):
        for seg_num in range(len(self.body_parts) - 1, 0, -1):
            new_x = self.body_parts[seg_num - 1].xcor()
            new_y = self.body_parts[seg_num - 1].ycor()
            self.body_parts[seg_num].goto(new_x, new_y)    
    
    def move_forward(self):
        self.head.forward(MOVE_DISTANCE)
    
    def move_up(self):
        if self.head.heading() == DOWN:
            pass
        else:
            self.head.setheading(UP)
    
    def move_down(self):
        if self.head.heading() == UP:
            pass
        else:
            self.head.setheading(DOWN)
    
    def move_left(self):
        if self.head.heading() == RIGHT:
            pass
        else:
            self.head.setheading(LEFT)
    
    def move_right(self):
        if self.head.heading() == LEFT:
            pass
        else:
            self.head.setheading(RIGHT)
    
    
    
    
    
    
    
    
    
        
  