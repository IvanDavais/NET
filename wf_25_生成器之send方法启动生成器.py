def create_num(num):
	a, b = 0, 1
	now_num = 0
	while now_num < num:
		# 注意：yield a的动作是将a的值传递到14行中的next()方法中，yield本身是没有值的，
		# 但是send()方法是可以将参数传递给yield a, 换言之，就是yield a = send传递的参数
		res = yield a
		print(res)
		a, b = b, a+b
		now_num += 1

temp = create_num(10)

x = next(temp)
print(x)
# 注意：！！send不能作为第一个启动生成器的方法，因为代码会从第1行开始执行，而不是直接从yield开始执行，所# 以没有人接受send传递的参数，这样程序崩,如果想用的话应该使用send(None)
send_display = temp.send("我的值就是res=yield的值")
print(send_display)
