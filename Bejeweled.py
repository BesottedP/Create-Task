import turtle
import time

while True:
    turtle.tracer(0,0)

    painter = turtle.Turtle()
    painter.hideturtle()
    turtle.hideturtle()
    painter.pensize(2)
    painter.color("white")

    screen = turtle.Screen()
    screen.setup(852,531)
    screen.bgpic("background_3x.gif")

    # Game box / boundaries
    painter.penup()
    painter.goto(-130, -215)
    painter.pendown()
    painter.right(45)
    painter.circle(325, 360, 4)

    # Game title box
    painter.penup()
    painter.goto(-400, 175)
    painter.setheading(0)
    painter.pendown()

    for a in range(70):
        if a < 10:
            painter.color("white")
        else:
            painter.color("black")
        for i in range(4):
            if i == 0 or i == 2:
                painter.forward(250-a)
            else:
                painter.forward(70-a)
            painter.left(90)
   
    painter.color("white")
    for i in range(4):
        if i == 0 or i == 2:
            painter.forward(250)
        else:
            painter.forward(70)
        painter.left(90)

    # Game title text
    painter.penup()
    painter.color("white")
    painter.goto(painter.xcor()+15, painter.ycor()+10)
    font = ("Arial", 30, "normal")
    painter.write("Turtle Crush", font=font)

    # Score text
    painter.penup()
    painter.goto(-315, 0)
    font = ("Arial", 20, "normal")
    painter.write("Score", font=font)

    painter.penup()
    painter.goto(-400, painter.ycor()-50)
    painter.pendown()
    for i in range(4):
        if i == 0 or i == 2:
            painter.forward(250)
        else:
            painter.forward(50)
        painter.left(90)

    # How to play text
    painter.penup()
    painter.goto(-415, -210)
    font = ("Arial", 10, "normal")
    painter.write('''
    
    How to play:
    Make matches of three or more objects. 
    To make matches, click on an object you 
    want to move, and use W,A,S, and D to 
    move it in the desired direction. Matches
    can only be made with adjacent objects.
    The objective is to get the highest score 
    possible in the allotted time ''', font=font)

    #Start text
    start_turtle = turtle.Turtle()
    start_turtle.hideturtle()
    start = False
    turtle.tracer(1,1)
    while start == False:
        start_turtle.penup()
        start_turtle.color("white")
        start_turtle.goto(-355, 140)
        font = ("Arial", 17, "normal")
        start_turtle.write("Press P to Start", font=font)
        time.sleep(.5)
        start_turtle.clear()
        time.sleep(.5)
    turtle.tracer(0,0)

    turtle.update()
    turtle.clear()
