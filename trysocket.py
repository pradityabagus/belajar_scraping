import socket

usedSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
usedSocket.connect(('data.pr4e.org', 80))

request = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n'.encode()
usedSocket.send(request)

while True:
    data = usedSocket.recv(512)
    if (len(data)<1):
        break
    print(data.decode())

usedSocket.close()