def addingNumbers(grid):
	#this part adds in the numbers to each row making sure that none of them
	#are duplicating.
	for x in range(9):
		for y in range(9):
			if x == 0 and y == 0:
				grid[x][y] = randint(1,9)
				continue
			elif x == 0:
                            newNumber = randint(1,9)
                            while newNumber in grid[x]:
                                    newNumber = randint(1,9)
                            grid[x][y] = newNumber
                            continue
                        elif x != 0:
                            holder = []
                            for i in range(9):
                                holder.append(grid[i][y])
                            newNumber = randint(1,9)
                            while (newNumber in grid[x]) and (newNumber in holder):
                                newNumber = randint(1,9)
                            grid[x][y] = newNumber
                            continue

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
