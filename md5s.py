import socket, hashlib

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Server listening...")

while True:
    client, addr = server.accept()
    data = client.recv(1024).decode()
    client.send(hashlib.md5(data.encode()).hexdigest().encode())
    client.close()
