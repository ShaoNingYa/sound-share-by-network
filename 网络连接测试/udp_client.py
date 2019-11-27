# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# import socket
#
# socket_handle = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# for data in [b'Michael', b'Tracy', b'Sarah']:
#     # 发送数据:
#     socket_handle.sendto(data, ('127.0.0.1', 9999))
#     # 接收数据:
#     print(socket_handle.recv(1024).decode('utf-8'))
#
# socket_handle.close()


import socket
def main():
    # 1创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.绑定一个本地信息
    localaddr = ("",7788) # 必须绑定自己电脑IP和port
    udp_socket.bind(localaddr)
    # 3.接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        # recv_data存储元组（接收到的数据，（发送方的ip,port））
        recv_msg = recv_data[0] # 信息内容
        send_addr = recv_data[1] # 信息地址
        # 4.打印接收到的数据
        # print(recv_data)
        print("信息来自:%s 内容是:%s" %(str(send_addr),recv_msg.decode("gbk")))
    # 5.退出套接字
    udp_socket.close()
if __name__ == "__main__":
    main()