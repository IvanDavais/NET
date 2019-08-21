""" 判断一个对象是否可以被迭代，首先看这个对象的类中是否有__iter__方法，如果有，则可以被迭代
    判断一个对象是否可以使用for循环来遍历，则在这个对象可以被迭代的基础上，看这个对象的类中的
    __iter__方法是否可以返回一个迭代器中的__next__方法的返回值，在该程序中，MyClassMate中的
    __iter__方法返回了MyClassIterator（这是一个迭代器，因为它同时拥有__iter__方法和__next__
    方法）中__next__方法的返回值。在MyClassIterator中，通过init方法获得MyClassMate的obj引用，从而
    使用obj引用来调用MyClassMate中的属性self.names,从而能打印self.names列表中的名字，并返回给MyClassMate
    中的__iter__方法，从而达到遍历self.names这个list
"""
import time

class MyClassMate(object):
	def __init__(self):
		self.names = list()

	def add(self, name):
		self.names.append(name)

	def __iter__(self):
		
		return MyClassIterator(self)

class MyClassIterator(object):
	def __init__(self, obj):
		self.obj = obj
		self.current = 0

	def __iter__self():
		pass

	def __next__(self):
		if self.current < len(self.obj.names):
			item = self.obj.names[self.current]
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
