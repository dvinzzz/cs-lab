import socket

def caesar_cipher(text, shift):
    enc= ""
    for char in text:
        if char.isupper():
            
            enc += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            enc += char
    return enc

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(1)
print("Server listening...")

while True:
    client, addr = server.accept()
    data = client.recv(1024).decode().split(',')
    message, shift = data[0], int(data[1])
    client.send(caesar_cipher(message, shift).encode())
    client.close()
