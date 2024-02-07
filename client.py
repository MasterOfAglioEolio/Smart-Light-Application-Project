import socket

HOST = '172.30.1.26'  # all available interfaces
PORT = 1428

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    msg=input()
    s.send(msg.encode(encoding='utf_8', errors='strict'))
    data = s.recv(1024)
    print ('result: ' + data.decode())

# s.close()
