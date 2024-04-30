import socket
import pickle

s = socket.socket()
port = 56789

s.connect(('192.168.8.102', port))
data_bytes = s.recv(1024)
data = pickle.loads(data_bytes)

for key in data:
    print(f'{key} : {data[key]}')

s.close()

