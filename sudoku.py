from random import randint

def addingNumbers(grid):
    #this part adds in the numbers to each row making sure that none of them
    #are duplicating.
    for x in range(9):
        for y in range(9):
            print x,y
            if x > 0:
                holder = []
                for i in range(9):
                    holder.append(grid[i][x])
                print holder
                newNumber = randint(1,9)
                while newNumber in grid[x] or newNumber in holder:
                    print grid[x]
                    print holder
                    newNumber = randint(1,9)
                    print newNumber
                    raw_input(">")
                grid[x][y] = newNumber
            else:
                newNumber = randint(1,9)
                while newNumber in grid[x]:
                    newNumber = randint(1,9)
                grid[x][y] = newNumber

def printBoard(grid):
    #this part prints the board to the screen for visual feedback
    hline = "    "
    for i in range(1,10):
        hline += "%s   " %(i)
    hSeperator = "  +---+" + ("---+" * 8)
    vSeperator = "  |   |" + ("   |" * 8)
    print hline
    print hSeperator
    for y in range(9):
        print vSeperator
        print (y + 1),
        for x in range(9):
            print ("| %s" % (grid[x][y])),
        print "|"
        print vSeperator
        print hSeperator

def makeGameBoard(grid):
    #this part makes the grid that contains the numbers
    for i in range(9):
        grid.append([])
        for l in range(9):
            grid[i].append("")

grid = []
raw_input("Making Game Board....")
makeGameBoard(grid)
raw_input("puting in numbers....")
addingNumbers(grid)
raw_input("printing board....")
printBoard(grid)
raw_input("finished")
