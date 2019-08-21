#coding=utf-8
import socket
def main():
    # 创建一个udp套接字
	udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	while True:

		# 使用udp套接字收发信息
		dest_addr = ('192.168.76.1', 8080)
		send_data = input("please enter what you want say: ")
		if send_data == "exit":
			break
		udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
	    
	    # 等待接受对方发送的数据
		recv_data = udp_socket.recvfrom(1024)
		
		print(recv_data[0].decode('gbk'))
		print(recv_data[1])

    # 关闭udp套接字
	udp_socket.close()

if __name__ == '__main__':
	main()
