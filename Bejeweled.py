# fuck you, your code is mine. We live in a communist world here
import random as rand
import turtle as t
import numpy as np

# box time
wn = t.Screen()
wn.bgcolor("white")
wn.setup(700, 700)

# genetically mutating a turtle
drawer = t.Turtle()
drawer.penup()
drawer.shapesize(10)
drawer.color("white")

# around the world
size = 10
list = np.zeros((size, size), dtype=int)
selected_gem = (None, None)  # Tuple of (row, col)

# i wanna fill wes' slots
def fillSlots():
    for row in range(size-1, -1, -1):
        for column in range(size-1, -1, -1):
            if (list[row][column] == 0):
                list[row][column] = rand.randint(1, 5)

# holy fucking shit i dont want to explain this code.
def swap(direction):
    temp = list[selected_gem[0]][selected_gem[1]]
    try:
        match direction:
            case "down":
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]+1][[selected_gem[1]]]
                list[selected_gem[0]+1][[selected_gem[1]]] = temp
                if (checkMatchHor() == False and checkMatchVert() == False):
                    list[selected_gem[0]+1][[selected_gem[1]]
                                            ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
            case "up":
                if (selected_gem[0] == 0):
                    raise Exception  # suicide
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]-1][[selected_gem[1]]]
                list[selected_gem[0]-1][[selected_gem[1]]] = temp
                if (checkMatchHor() == False and checkMatchVert() == False):
                    list[selected_gem[0]-1][[selected_gem[1]]
                                            ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
            case "left":
                if (selected_gem[1] == 0):
                    raise Exception  # suicide sequel
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]][[selected_gem[1]-1]]
                list[selected_gem[0]][[selected_gem[1]-1]] = temp
                if (checkMatchHor() == False and checkMatchVert() == False):
                    list[selected_gem[0]][[selected_gem[1]-1]
                                          ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
            case "right":
                list[selected_gem[0]][selected_gem[1]
                                      ] = list[selected_gem[0]][[selected_gem[1]+1]]
                list[selected_gem[0]][[selected_gem[1]+1]] = temp
                if (checkMatchHor() == False and checkMatchVert() == False):
                    list[selected_gem[0]][[selected_gem[1]+1]
                                          ] = list[selected_gem[0]][selected_gem[1]]
                    list[selected_gem[0]][selected_gem[1]] = temp
    except:  # retrieving the dead bodies
        print("Invalid Move")

# i dont wanna explain this either
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
    recurse = False
    for row in range(size-1, 0, -1):
        for column in range(0, size, 1):
            x = list[row][column]
            if (x == 0):
                list[row][column] = list[row-1][column]
                list[row-1][column] = 0
                if (list[row][column] != 0):
                    recurse = True
    if (recurse == True):  # side note: recursion can suck my ass
        dropJewel()

# segregate the turtles
def turtleChange(num):
    colors = ["white", "red", "green", "orange", "blue", "brown"]
    shapes = ["circle", "circle", "triangle", "square", "turtle", "arrow"]
    size = [1.5, 1, 1, 1, 1, 1]

    drawer.color(colors[num])
    drawer.shape(shapes[num])
    drawer.shapesize(size[num])

# bobby wrote this go ask him
def drawboard():
    global list, size
    for row in range(0, size, 1):
        for column in range(size-1, -1, -1):
            drawer.goto(column*50-200, row*50-200)
            turtleChange(list[(size-1)-row][column])
            drawer.stamp()

# dont you wanna play the game you dumb shit??
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

# WHAT THE FUCK IS A TUPLE
def select_gem(x, y):
    global selected_gem
    column = round((x+200)/50)
    row = round(9-((y+200)/50))
    selected_gem = (row, column)
    print(selected_gem)

# key binds (aka redundant pieces of shit just let me use arguments in onkeypress oml)
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
    print(list[0][0])
    print(list[-1][0])
    print(list[0][-1])
    print(list[-1][-1])

def selectedGem():
    print(selected_gem)

# your keyboard will stalk you now
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

# yeah you need this
startGame()
drawboard()

# keeps the game open so you can fucking play it
wn.mainloop()
