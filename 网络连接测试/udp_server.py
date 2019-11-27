#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

socket_handle = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
socket_handle.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')

while True:
    # 接收数据:
    data, address = socket_handle.recvfrom(1024)
    print('Received from %s:%s.' % address)
    reply = 'Hello, %s!' % data.decode('utf-8')
    socket_handle.sendto(reply.encode('utf-8'), address)
