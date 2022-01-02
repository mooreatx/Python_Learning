tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
			 
def printTable(list):
	colWidths = [0] * len(list)
	tab_cols = len(colWidths)
	max_rows = 0
	
	for y in range(len(list)):
		print(', '.join(list[y]))
	

printTable(tableData)