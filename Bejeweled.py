# imports
import random as rand
import turtle as t
import numpy as np
import time

# window setup
wn = t.Screen()
wn.bgcolor("white")
wn.setup(700, 700)

# turtle setup
drawer = t.Turtle()
drawer.penup()
drawer.shapesize(10)
drawer.color("white")

# global variables
game_start = False
score = 0
size = 10
list = np.zeros((size, size), dtype=int)
selected_gem = (None, None)  # Tuple of (row, col)

#fill
def fillSlots():
    for row in range(size-1, -1, -1):
        for column in range(size-1, -1, -1):
            if (list[row][column] == 0):
                list[row][column] = rand.randint(1, 5)
    drawboard()

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
                score += counter
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
                score += counter
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

    drawer.color(colors[num])
    drawer.shape(shapes[num])
    drawer.shapesize(tsize[num])

# bobby wrote this go ask him
def drawboard():
    tf = True
    while tf:
        t.tracer(0,0)
        global list, size
        for row in range(0, size, 1):
            for column in range(size-1, -1, -1):
                drawer.goto(column*50-200, 250-(row*50))
                turtleChange(list[row][column])
                drawer.stamp()
        t.update()
        tf = False

def drawswap(exception1, exception2): #put after the swap in the code above not before
    y=0
    while y<51:
        t.tracer(0,0)
        global list, size
        for row in range(0, size, 1):
            for column in range(size-1, -1, -1):
                drawer.goto(column*50-200, 250-(row*50))
                if (row, column)==exception2 and exception1[0] == exception2[0]: #across checking ::could be plus y
                    drawer.goto(column*50-200+y, 250-(row*50))
                if (row, column)==exception1 and exception1[0] == exception2[0]: #across checking  :: could be -y
                    drawer.goto(column*50-200-y, 250-(row*50))
                if (row, column)==exception2 and exception1[1] == exception2[1]: #could be -x
                    drawer.goto(column*50-200, 300-(row*50)-y)
                if (row, column)==exception1 and exception1[1] == exception2[1]: #could be +x
                    drawer.goto(column*50-200, 200-(row*50)+y)
                # print("test")
                turtleChange(list[row][column])
                drawer.stamp()
        
        t.update()
        drawer.clear()
        y+=2

def drawdrop():
    #checks how many spots each column needs to decend
    dropamount = []
    for row in range(0, size, 1):
        for column in range(0, size, 1):
            amount = 0
            for remcol in range(column+1, size, 1):
                if (list[column][row] != 0 and list[remcol][row] == 0):
                    amount += 1
            dropamount.append(amount)

    y = 0
    while y <= max(dropamount) * 50:
        t.tracer(0,0)
        for row in range(0, size, 1):
            for column in range(0, size, 1):
                drawer.goto(column*50-200, 250-(row*50))
                if y < dropamount[(column * 10) + row]*50:
                    drawer.goto(column*50-200, 250-(row*50)-y)  
                else:
                    drawer.goto(column*50-200, 250-(row*50)-(50*dropamount[column]))
                turtleChange(list[row][column])
                if list[row][column] != 0:
                    drawer.stamp()
        t.update()
        drawer.clear()
        y+=5

# start
def startGame():
    recurse = False
    if checkMatchHor() == True:
        recurse = True
    if checkMatchVert() == True:
        recurse = True
    if game_start == True:
        drawdrop()
    dropJewel()
    fillSlots()
    if game_start:
        time.sleep(0.25)
    if recurse == True:
        startGame()
        drawer.clear()
    drawer.clear()
    drawboard()

# gets the coordinates of the gem pressed
def select_gem(x, y):
    global selected_gem
    column = round((x+200)/50)
    row = round(9-((y+200)/50))
    selected_gem = (row, column)
    print(x, y)
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
game_start = True

wn.mainloop()
