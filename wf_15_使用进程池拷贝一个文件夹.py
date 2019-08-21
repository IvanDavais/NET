import os
import multiprocessing


def copy_files(filename, old_folder_name, new_folder_name):
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
	print("%s 拷贝完成" %filename)


def main():
	# 获取用户要copy的文件夹的名字
	old_folder_name = input("请输入你想copy文件夹的名字:")

	# 创建一个新的文件夹
	try:
		new_folder_name = old_folder_name +"[复件]"
		os.mkdir(new_folder_name)
	except:
		pass

	# 获取要拷贝文件夹中所有文件的名字
	files_name = os.listdir(old_folder_name)
	# 创建一个进程池
	pool = multiprocessing.Pool(5)
	
	# 向进程池中添加copy 文件的任务
	for filename in files_name:
		pool.apply_async(copy_files,(filename, old_folder_name, new_folder_name))
	
	pool.close()
	pool.join()
	

if __name__ == "__main__":
	main()
