def spam():
	global eggs
	eggs = 'change global name'

eggs = 'spam'
spam()
print(eggs)