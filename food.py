
from turtle import Turtle
import random


    

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.random_shape()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")    
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        randomX = random.randint(-420,420)
        randomY = random.randint(-280,280)
        self.goto(randomX,randomY)
        self.random_shape()
    
    def random_shape(self):
        a = random.randint(1,11)
        if a == 1:
            self.shape("./imgs/apple_01.gif")
        elif a == 2:
            self.shape("./imgs/kivy_01.gif")
        elif a == 3:
            self.shape('./imgs/bananas_01.gif')
        elif a == 4:
            self.shape('./imgs/blueberries_01.gif')
        elif a == 5:
            self.shape('./imgs/brombeere_01.gif')
        elif a == 6:
            self.shape('./imgs/cherries_01.gif')
        elif a == 7:
            self.shape('./imgs/coconut_01.gif')
        elif a == 8:
            self.shape('./imgs/granatapfel_01.gif')
        elif a == 9:
            self.shape('./imgs/grapes_01.gif')
        elif a == 10:
            self.shape('./imgs/lime_01.gif')
        elif a == 11:
            self.shape('./imgs/watermelon_01.gif')
        
            

        
        
        
        
        
        