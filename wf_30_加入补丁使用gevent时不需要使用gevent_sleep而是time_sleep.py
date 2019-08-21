"""从这个程序中可以学到：1.给这个程序打入monkey的补丁，使原来time.sleep依然可以在这个程序中正常运行 2.使用gevent.joinall方法提到了原来的g1 = join(), g2 = join()方法，且免去了g1 = gevent.spawn(f, "work1")等操作，方便很多"""
from gevent import monkey
import gevent 
import random
import time 

# 这个方法可以让time.sleep直接运行，原理是：这个方法会自动将time.sleep等耗时方法转化为
# gevent.sleep等方法

monkey.patch_all()
def f(work_name):
	for i in range(10):
		print(work_name, i)
		time.sleep(random.random())

gevent.joinall([
	gevent.spawn(f, "work1"),
	gevent.spawn(f, "work2")
])
