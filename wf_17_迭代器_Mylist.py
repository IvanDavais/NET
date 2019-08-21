class MyList(object):
	def __init__(self):
		self.container = []
	def add(self,item):
		self.container.append(item)
	def __iter__(self):
		pass

mylist = MyList()
from collections import Iterable
print(isinstance(mylist,Iterable))

