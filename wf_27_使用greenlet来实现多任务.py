from greenlet import greenlet
import time 

def test1():
	while True:
		print("---A---")
		gre2.switch()
		time.sleep(0.5)

def test2():
	while True:
		print("---B---")
		gre1.switch()
		time.sleep(0.5)

gre1 = greenlet(test1)
gre2 = greenlet(test2)

gre1.switch()
