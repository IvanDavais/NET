import os
import multiprocessing


def copy_files(q, filename, old_folder_name, new_folder_name):
	# 1.打开原文件夹中的文件
	old_f = open(old_folder_name + "/" +filename, "rb")
	# 2. 读取该文件
	content = old_f.read()
	# 3. 关闭原文件
	old_f.close()
	# 4. 打开新文件夹并创建相应文件
	new_f = open(new_folder_name + "/" +filename, "wb")
	# 5. 将第2步中的文件写入第4步创建的文件中
	new_f.write(content)
	# 6. 关闭新文件
	new_f.close()

	q.put(filename)

def main():
	# 获取用户要copy的文件夹的名字
	old_folder_name = input("请输入你想copy文件夹的名字:")

	# 创建一个新的文件夹
	new_folder_name = old_folder_name +"[复件]"
	try:
		os.mkdir(new_folder_name)
	except:
		pass

	# 获取要拷贝文件夹中所有文件的名字
	files_name = os.listdir(old_folder_name)
	# 创建一个进程池
	pool = multiprocessing.Pool(5)
	
	# 创建一个Queue
	q =multiprocessing.Manager().Queue()
	 

	# 向进程池中添加copy 文件的任务
	for filename in files_name:
		pool.apply_async(copy_files, args=(q, filename, old_folder_name, new_folder_name))
	
	pool.close()	
	# 要复制的文件总数
	sum_file_num = len(files_name)

	#print(sum_file_num)
	# 现在已复制的文件总数
	now_file_num = 0
	while True:
		file_name = q.get()
		print("已完成%s的复制" % file_name)
		now_file_num += 1
		print("现在的进度:%.2f%%" %(now_file_num*100/sum_file_num))
		if now_file_num >= sum_file_num:
			break

if __name__ == "__main__":
	main()
