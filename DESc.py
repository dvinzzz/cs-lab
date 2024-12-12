import socket
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad

localhost='127.0.0.1'
port=9090
key=b'8bytekey'
cipher=DES.new(key,DES.MODE_ECB)

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect((localhost,port))

msg=input("enter a message to encrypt using the DES algo")

encrypted_message=cipher.encrypt(pad(msg.encode(),DES.block_size))

client_socket.send(encrypted_message)

client_socket.close()