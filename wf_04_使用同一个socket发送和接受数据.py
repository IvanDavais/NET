from socket import *


def main():
	# 1. 创建一个套接字
	udp_socket = socket(AF_INET, SOCK_DGRAM)

	local_addr = ("",8081)
	udp_socket.bind(local_addr)	

	# 2. 获取对方的ip和port
	dest_ip = input("请输入你的ip地址： ")
	dest_port =int(input("请输入你的端口号: "))

	# 3.从键盘获取数据
	your_enter = input("请输入你想法送的内容：")

	# 4.发送数据
	udp_socket.sendto(your_enter.encode("utf-8"),(dest_ip, dest_port))

	# 5.接受数据
	receive_content = udp_socket.recvfrom(1025)
	print(receive_content[0].decode("utf-8"))

	udp_socket.close()

if __name__ == "__main__":
	main()
