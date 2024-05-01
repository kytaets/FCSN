import socket
import pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 65500

s.connect((socket.gethostname(), port))
data_bytes = s.recv(1024)
data = pickle.loads(data_bytes)

for key in data:
    print(f'{key} : {data[key]}')

s.close()
