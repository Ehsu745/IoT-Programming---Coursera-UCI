import socket
import sys

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.bind(("", 80))
except socket.error:
    print("fail to bind")
    sys.exit()
mysock.listen(5)

while True:
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    print("Got a requst!")
    if not data:
        break
    conn.sendall(data)

conn.close()
mysock.close()
