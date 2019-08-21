from socket import *
def main():
	# 1. 创建套接字
	udp_socket = socket(AF_INET, SOCK_DGRAM) 

	# 2. 绑定本地相关信息
	local_addr = ('',7878)
	udp_socket.bind(local_addr)

	# 3. 接受对方发出的数据
	rece_data = udp_socket.recvfrom(1024)

	# 4. 打印收到的文件
	print(rece_data[0].decode('gbk'))

	# 5. 关闭套接字
	udp_socket.close()

if __name__ == "__main__":
	main()
