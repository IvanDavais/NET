from multiprocessing import Pool
import os, time, random

def worker(msg):
	time_start = time.time()

	print("%s 开始执行，进程号为%d" %(msg, os.getpid()))
	time.sleep(random.random()*2)
	time_end = time.time()
	print(msg, "执行完毕，耗时%.4f" %(time_end - time_start))


def main():
	po = Pool(3)
	for i in range(10):
		po.apply_async(worker, (i,))
	print("start------------")
	po.close()
	po.join()
	print("end--------------")

if __name__ == "__main__":
	main()
