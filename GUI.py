# imports
import turtle as t

#turtle setup
board_turtle = t.Turtle()
board_turtle.penup()
board_turtle.hideturtle()

#fonts
title_font = ("Arial", 30, "normal")
scoretime_font = ("Arial", 20, "normal")

# Game box
tf = True
while tf:
    t.tracer(0,0)
    board_turtle.goto(-220, -220)
    board_turtle.pendown()
    board_turtle.right(45)
    board_turtle.circle(345, 360, 4)

    board_turtle.goto(-220, -220)
    board_turtle.setheading(0)
    

    # Game title box
    board_turtle.penup()
    board_turtle.goto(-500, 200)
    board_turtle.setheading(0)
    board_turtle.pendown()
    t.update()

    for a in range(70):
        if a < 10:
            board_turtle.color("white")
        else:
            board_turtle.color("black")
        for i in range(4):
            if i == 0 or i == 2:
                board_turtle.forward(250-a)
            else:
                board_turtle.forward(70-a)
            board_turtle.left(90)
   
    board_turtle.color("white")
    for i in range(4):
        if i == 0 or i == 2:
            board_turtle.forward(250)
        else:
            board_turtle.forward(70)
        board_turtle.left(90)


    tf = False

    # Game title text
    board_turtle.penup()
    board_turtle.color("white")
    board_turtle.goto(board_turtle.xcor()+15, board_turtle.ycor()+10)
    board_turtle.write("Turtle Crush", font=title_font)

    # Score text
    board_turtle.penup()
    board_turtle.goto(-415, 0)
    board_turtle.write("Score", font=scoretime_font)

    # Score box
    board_turtle.penup()
    board_turtle.goto(-500, board_turtle.ycor()-50)
    board_turtle.pendown()
    for i in range(4):
        if i == 0 or i == 2:
            board_turtle.forward(250)
        else:
            board_turtle.forward(50)
        board_turtle.left(90)

    # timer text
    board_turtle.penup()
    board_turtle.goto(-415, -125)
    board_turtle.write("Timer", font=scoretime_font)

    # timer box
    board_turtle.penup()
    board_turtle.goto(-500, board_turtle.ycor()-50)
    board_turtle.pendown()
    for i in range(4):
        if i == 0 or i == 2:
            board_turtle.forward(250)
        else:
            board_turtle.forward(50)
        board_turtle.left(90)

    # How to play text
    board_turtle.penup()
    board_turtle.goto(300, -85)
    font = ("Arial", 14, "normal")
    board_turtle.write('''
    
    How to play:
    Make matches of three or more 
    objects. To make matches, click 
    on an object you want to move, 
    and use W,A,S, and D to move it 
    in the desired direction. Matches
    can only be made with adjacent 
    objects.The objective is to get 
    the highest score possible in the 
    allotted time. 
    
    3 in a row = 600 points
    4 in a row = 3000 points
    5 in a row = 15000 points
    6 in a row = 87000 points
    ''', font=font)

#def made_leaderboard():
