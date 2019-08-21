import multiprocessing 


def download_data(q):
	data_list = [11, 22, 33]
	for data in data_list:
		q.put(data)
	print("已从网上下载完所有数据！")

def analysis_data(q):
	store_data = list()

	while True:
		data = q.get()
		store_data.append(data)
		if q.empty():
			break	

	print(store_data)

def main():
	q = multiprocessing.Queue(3)
	
	p1 = multiprocessing.Process(target=download_data, args=(q,))
	p2 = multiprocessing.Process(target=analysis_data, args=(q,))
	p1.start()
	p2.start()
if __name__ == "__main__":
	main()
