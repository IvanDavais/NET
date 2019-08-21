num_list = list()
a = 0
b = 1
num_list.append(a)

i = 0
while i < 10:
	a, b = b, a+b
	num_list.append(a)
	i += 1

for num in num_list:
	print(num)
