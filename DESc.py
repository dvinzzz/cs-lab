import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 12345))

message = input("Enter message to toggle case: ")
client.send(message.encode())

data = client.recv(1024).decode()
print(f"Toggled message: {data}")

client.close()