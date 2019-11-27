#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pyaudio
import time

socket_handle = socket.socket()
socket_handle.connect(('172.18.58.117', 9999))
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
# socket_handle.connect(('127.0.0.1', 9999))
audio_handle = pyaudio.PyAudio()
# 打开数据流
stream = audio_handle.open(format=FORMAT,
                           channels=CHANNELS,
                           rate=RATE,
                           output=True)
while True:
# for i in range(100):
    # 发送数据:
    # 接收数据:
    data = socket_handle.recv(4096)
    # print(data)
    # print("socket_handle.recv(1024)**")
    # time.sleep(0.1)

    # print(data[0])
    # print(i)
    stream.write(data)

# # 停止数据流
# stream.stop_stream()
# stream.close()
#
# # 关闭 PyAudio
# socket_handle.close()
# audio_handle.terminate()
#
# # -*-coding:utf-8-*-
#
# # 引入库
# import sys
#
# # 定义数据流块
# CHUNK = 1024
#
# # 只读方式打开wav文件
# wf = wave.open(r'./test.wav', 'rb')  # (sys.argv[1], 'rb')
#
# audio_handle = pyaudio.PyAudio()
#
# # 打开数据流
# stream = audio_handle.open(format=audio_handle.get_format_from_width(wf.getsampwidth()),
#                            channels=wf.getnchannels(),
#                            rate=wf.getframerate(),
#                            output=True)
#
# # 读取数据
# data = wf.readframes(CHUNK)
#
# # 播放
# while data != '':
#     stream.write(data)
#     data = wf.readframes(CHUNK)
#
# # 停止数据流
# stream.stop_stream()
# stream.close()
#
# # 关闭 PyAudio
# audio_handle.terminate()
