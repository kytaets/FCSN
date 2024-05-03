import socket
import json

port = 65500
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), port))

full_msg = ''
new_msg = True
while True:
    msg = s.recv(16)
    if new_msg:
        print(f"New message length: {msg[:HEADERSIZE]}")
        msg_len = int(msg[:HEADERSIZE])
        new_msg = False

    full_msg += msg.decode('utf-8')

    if len(full_msg) - HEADERSIZE == msg_len:
        print("full msg received\n")

        json_data = full_msg[HEADERSIZE:]
        dict_data = json.loads(json_data)
        for key in dict_data:
            print(f'{key} : {dict_data[key]}')

        new_msg = True
        full_msg = ''
