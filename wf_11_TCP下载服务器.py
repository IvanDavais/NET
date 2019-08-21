from socket import *

def send_file(tcp_server_socket, client_addr):
	# 接受顾客想要下载的文件名
	file_name = tcp_server_socket.recv(1024).decode("utf-8")

	# 打印顾客信息及顾客想要下载的文件名
	print("客户端%s 要下载的文件名: %s" %(client_addr, file_name))
	
	# 新建一个空的文件
	file_content = None
	try:
		f = open(file_name,"rb")
		file_content = f.read()
		f.close()
	except Exception as res:
		print("没有下载的文件(%s)" %file_name)
	
	# 发送用户想要下载的文件
	if file_content:
		tcp_server_socket.send(file_content)
		

def main():
	# 1. 建立套接字	
	tcp_server_socket = socket(AF_INET,SOCK_STREAM)
	# 2. 绑定本地信息	
	local_address = ("", 8083)
	tcp_server_socket.bind(local_address)

	# 3.将主动套接字变成被动套接字
	tcp_server_socket.listen(128)

	while True:	
		# 4.等电话
		new_client_socket, client_addr = tcp_server_socket.accept()
		
		# 5.接通电话，开始发送文件
		send_file(new_client_socket, client_addr)

		# 6. 关闭套接字
		new_client_socket.close()

	tcp_server_socket.close()


if __name__ == "__main__":
	main()
