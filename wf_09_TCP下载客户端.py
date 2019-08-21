import socket

def main():
	# 1.定义套接字
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# 2.获取服务器ip地址:
	server_ip = input("请输入服务器的ip地址: ")
	server_port = int(input("请输入服务器的端口号: "))

	# 3. 链接服务器
	tcp_socket.connect((server_ip, server_port))

	# 4. 获取下载为文件名
	download_file_name = input("请输入你想下载的文件的文件名: ")

	# 5. 将下载文件名发送到服务器
	tcp_socket.send(download_file_name.encode("utf-8"))

	# 6. 接受服务器发送过来的文件
	recv_data = tcp_socket.recv(1024)	

	# 7. 保存文件
	if recv_data:
		with open ("[接受]"+download_file_name, "wb") as f:
			f.write(recv_data)

	# 8. 关闭套接字	
	tcp_socket.close()

if __name__ == "__main__":
	main()
