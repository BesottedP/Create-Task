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
    drawboard()
    while y<51:
        t.tracer(0,0)
        global list, size
        for row in range(0, size, 1):
            for column in range(size-1, -1, -1):
                drawer.goto(column*50-200, 250-(row*50))
                if (row, column)==exception2 and exception1[0] == exception2[0]: #across checking ::could be plus y
                    drawer.goto(column*50-200+y, 250-(row*50))
                    print(1)
                if (row, column)==exception1 and exception1[0] == exception2[0]: #across checking  :: could be -y
                    drawer.goto(column*50-200-y, 250-(row*50))
                    print(2)
                if (row, column)==exception2 and exception1[1] == exception2[1]: #could be -x
                    drawer.goto(column*50-200, 300-(row*50)-y)
                    print(3)
                if (row, column)==exception1 and exception1[1] == exception2[1]: #could be +x
                    drawer.goto(column*50-200, 200-(row*50)+y)
                    print(4)
                # print("test")
                turtleChange(list[row][column])
                drawer.stamp()
        
        t.update()
        drawer.clear()
        y+=2
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
wn.onkeypress(drawboard, "u")
wn.listen()

# main functions
startGame()
drawboard()

wn.mainloop()
