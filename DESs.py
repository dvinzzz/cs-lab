import socket
from Crypto.Cipher import DES

localhost='127.0.0.1'
port=9090

key=b'8bytekey'
cipher=DES.new(key, DES.MODE_ECB)

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((localhost,port))
server_socket.listen(1)

client,address=server_socket.accept()

while True:
    data=client.recv(1024)
    if not data:
        break
    decrypted_data=cipher.decrypt(data).decode('utf-8').strip()

    
    print("the decrypted message is :",decrypted_data)

client.close()
server_socket.close()