import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

message = input("Enter message: ")
client.send(message.encode())
print("MD5 hash:", client.recv(1024).decode())

client.close()
