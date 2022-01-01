grid = [['.', '.', '.', '.', '.', '.'], #sublist 1
        ['.', 'O', 'O', '.', '.', '.'], #sublist 2
        ['O', 'O', 'O', 'O', '.', '.'], #sublist 3
        ['O', 'O', 'O', 'O', 'O', '.'], #sublist 4
        ['.', 'O', 'O', 'O', 'O', 'O'], #sublist 5
        ['O', 'O', 'O', 'O', 'O', '.'], #sublist 6
        ['O', 'O', 'O', 'O', '.', '.'], #sublist 7
        ['.', 'O', 'O', '.', '.', '.'], #sublist 8
        ['.', '.', '.', '.', '.', '.']] #sublist 9
		
for y in range(6): #This will run loop for a range of 6 values --columns--
    for x in range(9): #This will run loop for range of 9 values every time initial y loop range is ran --rows--
        print(grid[x][y], end='') #print grid sub list, loop x range --rows-- 9 times on each y --column-- range value. Then loops to the next y value and starts again 
    print('')
	
# The first index dictates which list value to use, and the second indicates the value within the list value.
