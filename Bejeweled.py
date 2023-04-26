# imports
import math
import random as rand
import turtle as t
import numpy as np
from PIL import Image

# window setup
wn = t.Screen()
wn.bgcolor("white")
wn.setup(1278, 796)
# image = Image.open('background_3.gif')
# image_resized = image.resize((1278,796))
# image_resized.save('background_3.gif')
wn.bgpic("background_1.gif")

#Create GUI
import GUI

# turtle setup
gem_turtle = t.Turtle()
gem_turtle.penup()
gem_turtle.hideturtle()
gem_turtle.shapesize(10)
gem_turtle.color("white")

score_turtle = t.Turtle()
score_turtle.penup()
score_turtle.color("white")
score_turtle.hideturtle()

timer_turtle = t.Turtle()
timer_turtle.penup()
timer_turtle.color("white")
timer_turtle.hideturtle()

# global variables
game_start = False
score = 0
size = 10
time_remaining = 30
timer_finished = False
list = np.zeros((size, size), dtype=int)
selected_gem = (None, None)

def updateTimer():
    global time_remaining, timer_finished
    timer_turtle.goto(-475, -175)
    timer_font = ("Arial", 30, "normal")
    timer_turtle.clear()
    if time_remaining == 0:
        timer_finished = True
        timer_turtle.write("0", font=timer_font)
        endGame(score)
    else:
        timer_turtle.write(str(time_remaining), font=timer_font)
        time_remaining -= 1
        timer_turtle.getscreen().ontimer(updateTimer, 1000)

def updateScore():
    score_turtle.goto(-475, -47)
    score_turtle.clear()
    score_font = ("Arial", 30, "normal")
    score_turtle.write(score, font=score_font)

def turtleChange(num):
    colors = ["white", "red", "green", "orange", "blue", "brown"]
    shapes = ["circle", "circle", "triangle", "square", "turtle", "arrow"]
    tsize = [1.5, 1, 1, 1, 1, 1]

    gem_turtle.color(colors[num])
    gem_turtle.shape(shapes[num])
    gem_turtle.shapesize(tsize[num])

# gets the coordinates of the gem pressed
def select_gem(x, y):
    global selected_gem
    column = round((x+200)/50)
    row = round(9-((y+200)/50))
    selected_gem = (row, column)

#fill
def fillSlots():
    for row in range(size-1, -1, -1):
        for column in range(size-1, -1, -1):
            if (list[row][column] == 0):
                list[row][column] = rand.randint(1, 5)

def swap(direction):
    if timer_finished == False:
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
        y+=3
        
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

def drawdrop():
    #checks how many spots each column needs to decend
    dropamount = []
    for column in range(0, size, 1):
        for row in range(0, size, 1):
            amount = 0
            for remrow in range(row, size, 1):
                if (list[remrow][column] == 0 and list[row][column] != 0):
                    amount += 1
            dropamount.append(amount)

    y = 0
    while y <= max(dropamount) * 50:
        t.tracer(0,0)
        for row in range(0, size, 1):
            for column in range(0, size, 1):
                gem_turtle.goto(column*50-200, 250-(row*50))
                if y < dropamount[column*10 + row]*50:
                    gem_turtle.goto(column*50-200, 250-(row*50)-y)  
                else:
                    gem_turtle.goto(column*50-200, 250-(row*50)-(50*dropamount[column*10 + row]))
                turtleChange(list[row][column])
                if list[row][column] != 0:
                    gem_turtle.stamp()
        t.update()
        gem_turtle.clear()
        y+=5

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
                score += (math.factorial(counter+1))*50
                for i in range(0, counter+1, 1):
                    list[row+i][column] = 0
    return matchMade

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

def texture_pack(x, y):
    a = 300
    if x > 325 and x < 350:
        if y > -150 and y < -105:
            a-=1      
    elif x > 515 and x < 540:
        if y > -150 and y < -105:
            a+=1

    b = a%3
    wn.bgpic('background_' + str(b) + '.gif')
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
    drawboard()
    
def endGame(player_score):
    if GUI.madeLeaderboard(player_score) == True:
        gem_turtle.clear()
        GUI.updateLeaderboard(GUI.promptName(), player_score)
    GUI.printLeaderboard()

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
wn.onscreenclick(texture_pack)
wn.listen()

# main functions
startGame()
game_start = True
wn.ontimer(updateTimer, 1000)
wn.mainloop()
