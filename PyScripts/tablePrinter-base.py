tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
			 
def printTable(list):
	for y in range(len(list)):
		for x in range(3):
			print(list[x][y])
	

printTable(tableData)