def collatz(number):
	if num % 2 == 0:
		return(number // 2)
	elif num % 2 == 1:
		return(3 * number + 1)
	else:
		print('Please only enter numbers')

num = int(input("Enter number: "))
response = collatz(num)
print(response)