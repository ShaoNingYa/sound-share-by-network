#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import pyaudio

socket_handle = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口:
socket_handle.bind(('172.18.58.117', 9999))

print('Bind UDP on 9999...')

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 0.1

audio_handle = pyaudio.PyAudio()

stream = audio_handle.open(format=FORMAT,
                           channels=CHANNELS,
                           rate=RATE,
                           input=True,
                           frames_per_buffer=CHUNK)
print("* recording")

while True:
    _data, address = socket_handle.recvfrom(4096)
    print('Received from %s:%s.' % address, _data)
    # frames = [parameter_setting]
    frames = []
    # for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    # for i in range(0, int(RATE / CHUNK)):
    # while address:
    #     data = stream.read(CHUNK)
    #     # frames.append(data)
    #     # print(len(data))
    #     socket_handle.sendto(data, address)
    data = stream.read(CHUNK)
    socket_handle.sendto(data, address)

stream.stop_stream()
stream.close()
p.terminate()
