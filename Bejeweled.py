# imports
import math
import random as rand
import turtle as t
import numpy as np
import time
from PIL import Image

# window setup
wn = t.Screen()
wn.bgcolor("white")
wn.setup(1278, 796)
image = Image.open('background_3x.gif')
image_resized = image.resize((1278,796))
image_resized.save('background_3x.gif')

wn.bgpic("background_3x.gif")

# turtle setup
gem_turtle = t.Turtle()
gem_turtle.penup()
gem_turtle.shapesize(10)
gem_turtle.color("white")

board_turtle = t.Turtle()
board_turtle.penup()

score_turtle = t.Turtle()
score_turtle.penup()
score_turtle.color("white")

timer_turtle = t.Turtle()
timer_turtle.penup()
timer_turtle.color("white")


# global variables
game_start = False
score = 0
size = 10
list = np.zeros((size, size), dtype=int)
selected_gem = (None, None)  # Tuple of (row, col)

# Game box / boundaries
tf = True
while tf:
    t.tracer(0,0)
    board_turtle.goto(-220, -220)
    board_turtle.pendown()
    board_turtle.right(45)
    board_turtle.circle(345, 360, 4)

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
    font = ("Arial", 30, "normal")
    board_turtle.write("Turtle Crush", font=font)

    # Score text
    board_turtle.penup()
    board_turtle.goto(-415, 0)
    font = ("Arial", 20, "normal")
    board_turtle.write("Score", font=font)

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


#fill
def fillSlots():
    for row in range(size-1, -1, -1):
        for column in range(size-1, -1, -1):
            if (list[row][column] == 0):
                list[row][column] = rand.randint(1, 5)

def updateScore():
    score_turtle.clear()
    score_font = ("Arial", 30, "normal")
    score_turtle.goto(-475, -47)
    score_turtle.write(score, font=score_font)

def swap(direction):
    temp = list[selected_gem[0]][selected_gem[1]]
    try:
        if direction == "down":
                if (selected_gem[0] == size-1):
                        raise Exception
                selected_gem2 = (selected_gem[0]+1, selected_gem[1])
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]+1][[selected_gem[1]]]
                list[selected_gem[0]+1][[selected_gem[1]]] = temp
                drawswap(selected_gem, selected_gem2)
                if (checkMatchHor() == False and checkMatchVert() == False):
                    list[selected_gem[0]+1][[selected_gem[1]]
                                            ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
                    drawswap(selected_gem, selected_gem2)
        elif direction == "up":
                if (selected_gem[0] == 0):
                    raise Exception
                selected_gem2 = (selected_gem[0]-1, selected_gem[1])
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]-1][[selected_gem[1]]]
                list[selected_gem[0]-1][[selected_gem[1]]] = temp
                drawswap(selected_gem2, selected_gem)
                if (checkMatchHor() == False and checkMatchVert() == False):
                    list[selected_gem[0]-1][[selected_gem[1]]
                                            ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
                    drawswap(selected_gem2, selected_gem)
        elif direction == "left":
                if (selected_gem[1] == 0):
                    raise Exception
                selected_gem2 = (selected_gem[0], selected_gem[1]-1)
                drawswap(selected_gem, selected_gem2)
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]][[selected_gem[1]-1]]
                list[selected_gem[0]][[selected_gem[1]-1]] = temp
                if (checkMatchHor() == False and checkMatchVert() == False):
                    drawswap(selected_gem, selected_gem2)
                    list[selected_gem[0]][[selected_gem[1]-1]
                                          ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp

        elif direction == "right":
                if (selected_gem[1] == size-1):
                    raise Exception
                selected_gem2 = (selected_gem[0], selected_gem[1]+1)
                drawswap(selected_gem2, selected_gem)
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]][[selected_gem[1]+1]]
                list[selected_gem[0]][[selected_gem[1]+1]] = temp
                if (checkMatchHor() == False and checkMatchVert() == False):
                    drawswap(selected_gem2, selected_gem)
                    list[selected_gem[0]][[selected_gem[1]+1]
                                          ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
    except:
        print("Invalid Move")                
    startGame()


# checks for matches
def checkMatchHor():
    global score
    matchMade = False
    for row in range(0, size, 1):
        for column in range(0, size-1, 1):
            counter = 0
            for remainingcol in range(1, size-column, 1):
                if list[row][column] == list[row][column+remainingcol]:
                    counter += 1
                else:
                    break
            if (counter >= 2):
                matchMade = True
                print(counter)
                score += (math.factorial(counter+1))*50
                for i in range(0, counter+1, 1):
                    list[row][column+i] = 0
    return matchMade

# read above comment
def checkMatchVert():
    global score
    matchMade = False
    for column in range(0, size, 1):
        for row in range(0, size-1, 1):
            counter = 0
            for remainingrow in range(1, size-row, 1):
                if list[row][column] == list[row+remainingrow][column]:
                    counter += 1
                else:
                    break
            if (counter >= 2):
                matchMade = True
                print(counter)
                score += (math.factorial(counter+1))*50
                for i in range(0, counter+1, 1):
                    list[row+i][column] = 0
    return matchMade

# i forget how this works, just think gravity ig
def dropJewel():
    for row in range(size-1, 0, -1):
        for column in range(0, size, 1):
            x = list[row][column]
            if (x == 0):
                list[row][column] = list[row-1][column]
                list[row-1][column] = 0
                if (list[row][column] != 0):
                    dropJewel()

# segregate the turtles
def turtleChange(num):
    colors = ["white", "red", "green", "orange", "blue", "brown"]
    shapes = ["circle", "circle", "triangle", "square", "turtle", "arrow"]
    tsize = [1.5, 1, 1, 1, 1, 1]

    gem_turtle.color(colors[num])
    gem_turtle.shape(shapes[num])
    gem_turtle.shapesize(tsize[num])

# bobby wrote this go ask him
def drawboard():
    tf = True
    while tf:
        t.tracer(0,0)
        global list, size
        for row in range(0, size, 1):
            for column in range(size-1, -1, -1):
                gem_turtle.goto(column*50-200, 250-(row*50))
                turtleChange(list[row][column])
                gem_turtle.stamp()
        t.update()
        tf = False

def drawswap(exception1, exception2): #put after the swap in the code above not before
    y=0
    while y<51:
        t.tracer(0,0)
        global list, size
        for row in range(0, size, 1):
            for column in range(size-1, -1, -1):
                gem_turtle.goto(column*50-200, 250-(row*50))
                if (row, column)==exception2 and exception1[0] == exception2[0]: #across checking ::could be plus y
                    gem_turtle.goto(column*50-200+y, 250-(row*50))
                if (row, column)==exception1 and exception1[0] == exception2[0]: #across checking  :: could be -y
                    gem_turtle.goto(column*50-200-y, 250-(row*50))
                if (row, column)==exception2 and exception1[1] == exception2[1]: #could be -x
                    gem_turtle.goto(column*50-200, 300-(row*50)-y)
                if (row, column)==exception1 and exception1[1] == exception2[1]: #could be +x
                    gem_turtle.goto(column*50-200, 200-(row*50)+y)
                # print("test")
                turtleChange(list[row][column])
                gem_turtle.stamp()
        
        t.update()
        gem_turtle.clear()
        y+=2

def drawdrop():
    #checks how many spots each column needs to decend
    dropamount = []
    dropindex = []
    for column in range(0, size, 1):
        amount = 0
        index = -1
        for row in range(0, size-1, 1):
            if (list[row][column] == 0):
                amount += 1
                if (index == -1):
                    index = row
        dropamount.append(amount)
        dropindex.append(index)

    y = 0
    while y <= max(dropamount) * 50:
        t.tracer(0,0)
        for row in range(0, size, 1):
            for column in range(0, size, 1):
                gem_turtle.goto(column*50-200, 250-(row*50))
                if row < dropindex[column]:
                    if y < dropamount[column]*50:
                        gem_turtle.goto(column*50-200, 250-(row*50)-y)  
                    else:
                        gem_turtle.goto(column*50-200, 250-(row*50)-(50*dropamount[column]))
                turtleChange(list[row][column])
                if list[row][column] != 0:
                    gem_turtle.stamp()
        t.update()
        gem_turtle.clear()
        y+=5
    time.sleep(0.15)

# start
def startGame():
    global score
    recurse = False
    if checkMatchHor() == True:
        recurse = True
    if checkMatchVert() == True:
        recurse = True
    if game_start == True:
        drawdrop()
    if game_start == False:
        score=0
    dropJewel()
    fillSlots()
    updateScore()
    if recurse == True:
        startGame()
        gem_turtle.clear()
    gem_turtle.clear()
    drawboard()

# gets the coordinates of the gem pressed
def select_gem(x, y):
    global selected_gem
    column = round((x+200)/50)
    row = round(9-((y+200)/50))
    selected_gem = (row, column)
    print(selected_gem)

# key binds
def up():
    swap("up")
   
def left():
    swap("left")

def down():
    swap("down")

def right():
    swap("right")

def printBoard():
    print(list)

def test():
    global score
    print(score)

def selectedGem():
    print(selected_gem)

# listening for key presses
wn.onscreenclick(select_gem)
wn.onkeypress(up, "w")
wn.onkeypress(left, "a")
wn.onkeypress(down, "s")
wn.onkeypress(right, "d")

wn.onkeypress(printBoard, "p")
wn.onkeypress(test, "t")
wn.onkeypress((selectedGem), "g")
wn.onkeypress(drawboard, "u")
wn.listen()

# main functions
startGame()
drawboard()

game_start = True

wn.mainloop()
