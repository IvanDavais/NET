from socket import *

def main():
	# 创建套接字
	tcp_socket = socket(AF_INET, SOCK_STREAM)

	# 连接客户端
	server_ip = input("请输入服务器的ip: ")
	server_port = int(input("请输入服务器的port: "))
	tcp_socket.connect((server_ip, server_port))	

	# 发送信息
	send_msg = input("请输入你发送的内容:")
	tcp_socket.send(send_msg.encode("utf-8"))

	# 接受信息
	recv_msg = tcp_socket.recvfrom(1024)
	print(recv_msg[0].decode("utf-8"))

	# 关闭套接字
	tcp_socket.close()


if __name__ == "__main__":
	main()
