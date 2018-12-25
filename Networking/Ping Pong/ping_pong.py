import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('35.157.111.68', 10015))
time.sleep(1)


buffer = sock.recv(1024).decode()
print(buffer.strip())
buffer = '{0}\n'.format(buffer.strip().split(' ')[-1]).encode()

while buffer[:-1].isdigit():
    sock.send(buffer)

    buffer = sock.recv(200).decode()
    print(buffer.strip())
    buffer = '{0}\n'.format(buffer.strip().split(' ')[-1]).encode()
