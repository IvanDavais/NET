"""
注意在这个方法，没有创建任何列表，占用的空间非常小，只是在生成Fibonacci时才占用了一定的空间，
即15 - 22 行占用了点空间，其他的代码很少占用空间，对比上一个代码，假设要创建Fibonacci数列1万个
的话，前一个代码则需要创建一个有1万个元素的list，而这个代码则不需要。
"""
class Fibonacci(object):
	def __init__(self, sum_num):
		self.sum_num = sum_num
		self.now_num = 0
		self.a = 0
		self.b = 1

	def __iter__(self):
		return self
	
	def __next__(self):
		temp = self.a
		if self.now_num < self.sum_num:
			self.a, self.b = self.b, self.a+self.b
			self.now_num += 1
			return temp
		else:
			raise StopIteration

li = list(Fibonacci(15))
print(li)

tp = tuple(Fibonacci(6))
print(tp)
