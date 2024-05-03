import socket
import json

port = 65500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket successfully created!')

s.bind((socket.gethostname(), port))
print(f'Socket bind to port {port}')

s.listen(5)
print('Socket is listening')

meteo_data = {
    'station_id': 'WTHR1234',
    'temperature': 21.2,
    'humidity': 56.3,
    'pressure': 30.1
}

HEADERSIZE = 10

while True:
    conn, addr = s.accept()
    print('Got connection from', addr)

    data_json = json.dumps(meteo_data)
    msg = f'{len(data_json):<{HEADERSIZE}}' + data_json

    conn.send(bytes(msg, "utf-8"))
