def collatz(number):				#Function code snippet, invoked by while loop
	if num % 2 == 0:				#If number does not divides without remainder, run this code
		print(number // 2)
		return number // 2
	elif num % 2 == 1:				#If number divides with remainder, run this code
		print(3 * number + 1)
		return 3 * number + 1


num = int(input("Enter number: "))	#Start of code, function 'collatz' only invoked when called
while num != 1:						#After num input, run while loop that calls collatz function until number entered equals 1
	num = collatz(num)
