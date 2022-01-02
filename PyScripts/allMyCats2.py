catNames = [] # list
while True:
	print('Enter the name of cat ' + str(len(catNames) + 1) + # Takes current numbers of values in list along with addition of 1
		' (or enter nothing to stop):') 
	name = input() # input value that will go into list
	if name == '':
		break	# end while loop if no input provided
	catNames = catNames + [name] # list concatenation, current list value plus new value index provided from name input
print('The cat names are:')
for name in catNames:
	print(' ' + name)