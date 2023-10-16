

import time
from turtle import Screen
from snake import Snake, random_color, preColors
from food import Food
from scoreboard import Scoreboard


import winsound
import tkinter
import turtle

mainloop = True
while mainloop:
    winsound.PlaySound('mainTheme.wav', winsound.SND_ASYNC)
    screen = Screen()
    screen.setup(width=900, height=900)
    screen.bgcolor("black")
    screen.title("Ultimate Snake")
    screen.tracer(0)

    screen.addshape('./imgs/apple_01.gif')
    screen.addshape('./imgs/kivy_01.gif')
    screen.addshape('./imgs/bananas_01.gif')
    screen.addshape('./imgs/blueberries_01.gif')
    screen.addshape('./imgs/brombeere_01.gif')
    screen.addshape('./imgs/cherries_01.gif')
    screen.addshape('./imgs/coconut_01.gif')
    screen.addshape('./imgs/granatapfel_01.gif')
    screen.addshape('./imgs/grapes_01.gif')
    screen.addshape('./imgs/lime_01.gif')
    screen.addshape('./imgs/watermelon_01.gif')

    # my sweet little classes
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    # listen on keys
    screen.onkey(snake.move_up, "w")
    screen.onkey(snake.move_down, "s")
    screen.onkey(snake.move_left, "a")
    screen.onkey(snake.move_right, "d")
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_left, "Left")
    screen.onkey(snake.move_right, "Right")   

    gameloop = True
    while gameloop:
        
        screen.update()     # update screen / drawings ezc,
        time.sleep(0.1)     # a bit of relaxing time for the human eyes
        screen.listen()     # listen to events
        screen.title("Score: " + scoreboard.title_score())
        
        
        
        snake.move_body()   # let the snakes body move the same as the head of the snake
        snake.move_forward()    # let it run 
        scoreboard.show_score() # show the scoreboard
        
        # Detect collision with food
        if snake.head.distance(food) < 17:
            food.refresh()
            snake.extend()
            scoreboard.set_score_plus()
        
        # Detect collision with wall
        if snake.head.xcor() > 440 or snake.head.xcor() < -440 or snake.head.ycor() > 440 or snake.head.ycor() < -440:
            gameloop = False
            scoreboard.game_over()
        
        # Detect collision with tail
        for segment in snake.body_parts[1:]:
            segment.color(random_color(preColors))  # RAINBOW SCHLANGE
            
            if snake.head.distance(segment) < 15:
                gameloop = False
                scoreboard.game_over()
    time.sleep(2)
    screen.clear()
