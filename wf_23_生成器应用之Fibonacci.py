def create_num(num):
	a, b = 0, 1
	current_num = 0
	while current_num < num:
		yield a
		a, b = b, a+b
		current_num += 1
	
obj = create_num(10)
for num in obj:
	print(num)
