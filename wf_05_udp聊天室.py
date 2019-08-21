from socket import *

def send_msg(udp_socket):
	msg = input("请输入你想发送的信息: ")
	des_ip = input("对方的IP:")
	des_port =int(input("对方的port:"))
	udp_socket.sendto(msg.encode("utf-8"),(des_ip,des_port))
	

def recv_msg(udp_socket):
	recv_msg = udp_socket.recvfrom(1024)
	print("%s : %s" %(recv_msg[1], recv_msg[0].decode("utf-8")))


def main():
	udp_socket = socket(AF_INET, SOCK_DGRAM)
	udp_socket.bind(("", 7880))
	while True:

		print("1:发送消息")
		print("2.接受消息")
		print("3.准备退出")
		
		user_enter = input("请选择功能：")

		if user_enter == "1":
			send_msg(udp_socket)
		elif user_enter == "2":
			recv_msg(udp_socket)
		elif user_enter == "3":
			break
		else:
			print("您的输入有误，请重新输入:")


if __name__ == "__main__":
	main()
