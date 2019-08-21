import socket

def main():
	# 买个手机，（创建套接字）
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# 插入手机卡 (绑定本地信息)
	tcp_server_socket.bind(("", 8082))
	
	# 将手机调成铃声模式 (让默认套接字由主动变成被动）
	tcp_server_socket.listen(128)


	# 循环目的：调用多次accept，从而为多个客户端服务
	while True:
		print("1. 有新用户接入：")
		# 等待别人打电话（等待客户端连接：）
		new_client_socket, client_addr = tcp_server_socket.accept()

		print("2  新用户%s 发送的数据为:" %str(new_client_socket))

		# 循环目的：为同一个用户提供多次服务	
		while True:
			# 接受客户端发送过来的请求：
			recv_data = new_client_socket.recv(1024)
			print((recv_data).decode("utf-8"))

			if recv_data:
				new_client_socket.send("ni hao wan fan ".encode("utf-8"))
			else:
				break

		new_client_socket.close()
	tcp_server_socket.close()



if __name__ == "__main__":
	main()
