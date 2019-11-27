#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pyaudio

socket_handle = socket.socket()

# 绑定端口:
socket_handle.bind(('172.18.58.117', 8976))
socket_handle.listen(5)  # 最大连接数

print('Bind TCP on 8976...')

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 0.1

print("* recording")

while True:
    # _data, address = socket_handle.recvfrom(4096)
    conn, address = socket_handle.accept()
    msg = "连接成功"
    conn.send(msg.encode())
    audio_handle = pyaudio.PyAudio()

    stream = audio_handle.open(format=FORMAT,
                               channels=CHANNELS,
                               rate=RATE,
                               input=True,
                               frames_per_buffer=CHUNK)
    print(address, "已连接")
    while True:
        data = stream.read(CHUNK)
        # print(len(data))
        conn.send(data)
        if data == b'exit':
            break
    conn.close()

stream.stop_stream()
stream.close()
p.terminate()
