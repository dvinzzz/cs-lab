import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

message = input("Enter message: ")
shift = input("Enter shift value: ")
client.send(f"{message},{shift}".encode())

print("Encrypted message:", client.recv(1024).decode())
client.close()
