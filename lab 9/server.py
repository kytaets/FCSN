import socket
import pickle

s = socket.socket()
print('Socket successfully created!')
port = 56789

s.bind(('', port))
print(f'Socket bind to port {port}')

s.listen(5)
print('Socket is listening')

meteo_data = {
    'station_id': 'WTHR1234',
    'temperature': 21.2,
    'humidity': 56.3,
    'pressure': 30.1
}

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)
    data_bytes = pickle.dumps(meteo_data)
    conn.send(data_bytes)
    conn.close()
