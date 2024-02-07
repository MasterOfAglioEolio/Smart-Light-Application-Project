import time
import numpy as np
import socket
import sys
import neopixel
import os
import config
from rpi_ws281x import *
HOST = '172.30.1.26'  # all available interfaces
PORT = 1428

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print('Bind Failed. Error code: ' + str(msg[0]) + ' Message: ' + msg[1])
    sys.exit()

print('Socket bind complete')

s.listen(10)
print('Socket now listening')
conn, addr = s.accept()
print('Connected')

count=0
np_data = np.array([])
temp_data=np.array([])

def start_stream(callback):
    print('Connected with ' + addr[0] + ':' + str(addr[1]))
    audio_data = conn.recv(1024)
    conn.sendall(audio_data)

    overflows = 0
    prev_ovf_time = time.time()
    while True:
        try:

            audio_data = conn.recv(1024)
            conn.sendall(audio_data)
            np_data = np.frombuffer(audio_data, dtype=np.float32)
            print(np_data)
            print(np_data.shape)
            callback(np_data)
        except IOError:
            overflows += 1
            if time.time() > prev_ovf_time + 1:
                prev_ovf_time = time.time()
                print('Audio buffer has overflowed {} times'.format(overflows))
    stream.stop_stream()
    stream.close()
    p.terminate()
