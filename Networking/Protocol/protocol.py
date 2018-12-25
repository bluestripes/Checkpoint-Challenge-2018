import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('35.157.111.68', 20076))

time.sleep(1)
buffer = sock.recv(1024)
print(buffer)

xor = None
i = 1
cmds = ['HELLO', 'XOR', '/usr/SeCret.txt']
for cmd in cmds:
    str = '{0} {1} {2}\n'.format(i, len(cmd), cmd)
    sock.send(str.encode())

    buffer = sock.recv(1024)
    print(buffer)
    i += 1
    if cmd == 'XOR':
        xor = int(buffer.strip().split()[-1], 16)

flag = ''
buffer = ''.join(buffer.decode().split()[2:]).split('0x')[1:]
for chunk in buffer:
    chunk = int(chunk, 16) ^ xor
    flag += chr(chunk >> 8) + chr(chunk & 0xff)
print(flag)
