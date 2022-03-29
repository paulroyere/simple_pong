# Simple Pong game using Python 3
# Turtle import is a default Python module for older versions... You needed to install python-tkinter if using Fedora 35

from tkinter.font import BOLD
import turtle
import os # module to interact with the operating system

# wn stands for Window
wn = turtle.Screen()
wn.title("Ultimate Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)

# this stops the window from updating
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup() # moves do not draw line
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup() # moves do not draw line
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # speed of animation
ball.shape("square")
ball.color("white")
ball.penup() # moves do not draw line
ball.goto(0, 0)

ball.dx = 0.1 # delta (change) in x coordinate
ball.dy = -0.1

# Pen (or scoring board)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260) # You can probably change the placing for that score
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))


# Paddle_a functions (up/down)
def paddle_a_up():
    y = paddle_a.ycor() # returning y coordinate
    y += 20 # adding 20 pixels to y
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor() # returning y coordinate
    y -= 20 # adding 20 pixels to y
    paddle_a.sety(y)

# Paddle_b functions (up/down)
def paddle_b_up():
    y = paddle_b.ycor() # returning y coordinate
    y += 20 # adding 20 pixels to y
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor() # returning y coordinate
    y -= 20 # adding 20 pixels to y
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up,"w") # when user presses w, paddle_a_up function gets called
wn.onkeypress(paddle_a_down,"s") 
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down") 



# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking (290, -290 is basically y coordinate added, 390 is x coordinate added)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # this will reverse the direction
        os.system("aplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        os.system("aplay explosion.wav&")
        pen.clear() # clears what is on the screen
        #pen.write("Player A: "+ str(score_a) +"  Player B: "+ str(score_b), align="center", font=("Courier", 24, "normal"))
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        os.system("aplay explosion.wav&")
        pen.clear() # clears what is on the screen
        #pen.write("Player A: "+ str(score_a) +"  Player B: "+ str(score_b), align="center", font=("Courier", 24, "normal"))
        pen.write("Player A: {} Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


    # Compare paddle & ball coordinates to have ball bounce back (this is going to be using the paddle position for the most part)
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
