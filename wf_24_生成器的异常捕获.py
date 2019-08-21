def create_num(num):
	a, b = 0, 1
	now_num = 0
	while now_num < num:
		yield a
		a, b = b, a+b
		now_num += 1
	# 注意此处return返回的值无法在next()方法中得到，而是在捕获异常时的参数.value才能得到此值
	return "ok"	
temp = create_num(10)

while True:
	try:
		x = next(temp)
		print(x)
	except StopIteration as e:
		print(e)
		# 此处的e.value就是返回上面return的值
		print("生成器的返回值为:%s" %e.value)
		break

