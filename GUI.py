# imports
import turtle as t
from PIL import Image

#Global Variables
leaderboardFile = "Turtle_Crush_Leaders.txt"

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

#Leaderboard----------------------------------------------------------------------------------

def getNames():
    names = []
    lb = open(leaderboardFile, "r") 

    for line in lb:
        player_name = ""
        index = 0
        while (line[index] != ","):
            player_name += line[index]
            index += 1
    
        names.append(player_name)

    lb.close()
    return names
    

def getScores():
  lb = open(leaderboardFile, "r")
 
  scores = []
  for line in lb:
    player_score = ""    
    index = 0
    while (line[index] != ","):
        index += 1
    index += 1    
    while(line[index] != "\n"):
      player_score += (line[index])
      index+=1
 
    scores.append(int(player_score))

  lb.close()
 
  return scores

def promptName():
    board_turtle.clear()
    board_turtle.up()
    board_turtle.goto(-300,0)
    board_turtle.write("You made the leaderboard!" + "\n" + "Enter your name into the terminal", font=title_font)
    return input("Enter name:")

def madeLeaderboard(player_score):
    lb_scores = getScores()

    if len(lb_scores) < 7 or player_score > lb_scores[6]:
        return True
    else:
        return False

def updateLeaderboard(playername, player_score):
    lb_names = getNames()
    lb_scores = getScores()
    
    index = 0
    for i in range(len(lb_scores)):
        if (lb_scores[index] < player_score):
            break
        else:
            index += 1
    
    lb_names.insert(index, playername)
    lb_scores.insert(index, player_score)
    
    if (len(lb_scores) > 7):
        lb_names.pop()
        lb_scores.pop()
    
    leaderboard_file = open(leaderboardFile, "w")

    index = 0
    for index in range(len(lb_scores)):
        leaderboard_file.write(lb_names[index] + "," + str(lb_scores[index]) + "\n")
    
    leaderboard_file.close()

def printLeaderboard():
    lb_names = getNames()
    lb_scores = getScores()

    board_turtle.clear()
    board_turtle.up()

    for index in range(len(lb_names)):
        if(index == 0):
            board_turtle.color("gold")
        elif(index == 1):
            board_turtle.color("silver")
        elif(index == 2):
            board_turtle.color("brown")
        else:
            board_turtle.color("white")

        board_turtle.goto(-200,200-(75*index))
        board_turtle.write(str(index + 1) + "\t" + lb_names[index] + "\t   " + str(lb_scores[index]), font=title_font)
    

# Change Background buttons
arrow_font = ("Arial", 20, "normal")

board_turtle.pensize(8)
board_turtle.hideturtle()
board_turtle.goto(360, -145)
board_turtle.write("Background", font=arrow_font)

def draw_arrow(xcor, ycor, heading, angle):
    board_turtle.up()
    board_turtle.goto(xcor,ycor)
    board_turtle.down()
    board_turtle.seth(heading)
    board_turtle.forward(30)
    board_turtle.right(angle)
    board_turtle.forward(30)

draw_arrow(350, -150, 135, 90)
draw_arrow(515, -150, 45, 270)



