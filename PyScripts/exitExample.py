import sys

while True:
	print('Type Exit to exit.')
	response = input()
	if response == 'Exit':
		sys.exit()
	print('You typed ' + response + '.')
	
