birthdays = {'Mom': '01/06/84', 'Jack': '12/13/16', 'Dad': '08/22/86'}

while True:
	print('Enter a name: (blank to quit)')
	name = input()
	if name == '':
		break
		
	if name in birthdays:
		print(birthdays[name] + ' is the birthday of ' + name)
	else:
		print('I do not have birthday information for ' + name)
		print('What is their birthday?')
		bday = input()
		birthdays[name] = bday
		print('Birthday database updated.')
	    