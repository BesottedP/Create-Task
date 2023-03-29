# imports
import random as rand
import turtle as t
import numpy as np

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
size = 10
list = np.zeros((size, size), dtype=int)
selected_gem = (None, None)  # Tuple of (row, col)

#fill 
def fillSlots():
    for row in range(size-1, -1, -1):
        for column in range(size-1, -1, -1):
            if (list[row][column] == 0):
                list[row][column] = rand.randint(1, 5)


def swap(direction):
    temp = list[selected_gem[0]][selected_gem[1]]
    try:
        if direction == "down": 
                selected_gem2 = (selected_gem[0]+1, selected_gem[1])
                drawboard(selected_gem, selected_gem2)
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]+1][[selected_gem[1]]]
                list[selected_gem[0]+1][[selected_gem[1]]] = temp
                
                if (checkMatchHor() == False and checkMatchVert() == False):
                    list[selected_gem[0]+1][[selected_gem[1]]
                                            ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
        elif direction == "up":
                if (selected_gem[0] == 0):
                    raise Exception 
                selected_gem2 = (selected_gem[0]-1, selected_gem[1])
                drawboard(selected_gem2, selected_gem)
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]-1][[selected_gem[1]]]
                list[selected_gem[0]-1][[selected_gem[1]]] = temp
                if (checkMatchHor() == False and checkMatchVert() == False):
                    list[selected_gem[0]-1][[selected_gem[1]]
                                            ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
        elif direction == "left":
                if (selected_gem[1] == 0):
                    raise Exception
                selected_gem2 = (selected_gem[0], selected_gem[1]-1)
                drawboard(selected_gem, selected_gem2)
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]][[selected_gem[1]-1]]
                list[selected_gem[0]][[selected_gem[1]-1]] = temp
                if (checkMatchHor() == False and checkMatchVert() == False):
                    list[selected_gem[0]][[selected_gem[1]-1]
                                          ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
        elif direction == "right":
                selected_gem2 = (selected_gem[0], selected_gem[1]+1)
                drawboard(selected_gem2, selected_gem)
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]][[selected_gem[1]+1]]
                list[selected_gem[0]][[selected_gem[1]+1]] = temp
                if (checkMatchHor() == False and checkMatchVert() == False):
                    list[selected_gem[0]][[selected_gem[1]+1]
                                          ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
    except:  # retrieving the dead bodies
        print("Invalid Move")

def drawswap(direction):
    if direction == "right":
        p = True
        while p:
            t.clear()
            

    if direction == "left":
        #TODO




# checks for matches
def checkMatchHor():
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
                for i in range(0, counter+1, 1):
                    list[row][column+i] = 0
    return matchMade

# read above comment
def checkMatchVert():
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
def startboard():
    t = True
    while t:
        t.tracer(0,0)
        global list, size
        for row in range(0, size, 1):
            for column in range(size-1, -1, -1):
                drawer.goto(column*-200, row*50-200)
                turtleChange(list[(size-1)-row][column])
                drawer.stamp()
                t.update()
        t = False

def drawboard(exception1, exception2): #put after the swap in the code above not before
    t = True
    while t:
        t.tracer(0,0)
        global list, size
        for row in range(0, size, 1):
            for column in range(size-1, -1, -1):
                drawer.goto(column*50-200, row*50-200)
                if (column*50-200, row*50-200)==exception2 and exception1[0] == exception2[0]: #across checking
                    drawer.goto(column*50-200-50, row*50-200)
                if (column*50-200, row*50-200)==exception1 and exception1[0] == exception2[0]: #across checking
                    drawer.goto(column*50-200+50, row*50-200)
                turtleChange(list[(size-1)-row][column])
                drawer.stamp()
                t.update()
        t = False

# start
def startGame():
    recurse = False
    fillSlots()
    if checkMatchHor() == True:
        recurse = True
    if checkMatchVert() == True:
        recurse = True
    dropJewel()
    fillSlots()
    if recurse == True:
        print()
        startGame()

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
    drawswap("right")

def printBoard():
    print(list)

def test():
    print(list[0][0])
    print(list[-1][0])
    print(list[0][-1])
    print(list[-1][-1])

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
wn.onkeypress(startboard, "u")
wn.listen()

# main functions
startGame()
startboard()

wn.mainloop()
