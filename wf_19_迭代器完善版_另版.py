import time
"""一个对象能不能迭代？首先看在创建这个对象的类中是不是有__iter__方法，如果有，
   那么接着看这个iter方法里是否可以调用迭代器对象(一个迭代器对象里必须拥有__iter__方法
   和__next__方法),如果有，则返回这个迭代器对象中__next__方法的返回值，在这个
   MyClassMate类中，1. 有__iter__方法，所以这个类创建的对象可以被迭代，2.这个
   类本身拥有__next__方法，所以这个类本身创建的对象可以作为迭代器对象，从而不需要
   再写一个迭代器，换一种说法：这个类用自身迭代了自身
"""
class MyClassMate(object):
	def __init__(self):
		self.names = list()
		self.current = 0

	def add(self, name):
		self.names.append(name)

	def __iter__(self):
		
		return self


	def __next__(self):
		if self.current < len(self.names):
			item = self.names[self.current]
			self.current += 1
			return item
		else:
			raise StopIteration


def main():
	myclassmata = MyClassMate()
	myclassmata.add("zhangsan")
	myclassmata.add("Lisi")
	myclassmata.add("Wangwu")
	for i in myclassmata:
		print(i)
		time.sleep(1)
if __name__ == "__main__":
	main()
