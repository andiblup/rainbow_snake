
from turtle import Turtle, Screen
from food import Food

#food = Food()
"""counterScore = []
screen = Screen()
screen.bgcolor("darkgrey")"""
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 250)
        self.color("purple")
        #self.write("Score: " + str(self.score), False, "center", ('Arial', 16, 'normal'))
    
    def return_score(self):
        return self.score
    
    def set_score_plus(self):
        self.score += 1
    
    def show_score(self):
        self.clear()
        self.write("Score: " + str(self.return_score()), False, "center", ('Arial', 16, 'normal'))
        
    def title_score(self):
        return str(self.score)
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=('Arial', 46, 'normal'))
    

"""score = Scoreboard()

score.hideturtle()
screen.exitonclick()"""

