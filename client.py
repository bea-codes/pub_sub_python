# Echo client program
import socket

HOST = '127.0.0.1'          # The remote host
PORT = 5050            # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # choice = input()                    # input no console
    # s.sendall(bytes(choice, 'utf-8'))   # transforma string em bytestream
    topico = input("nome do topico: ")
    while True:
        msg = input("digite a msg: ")
        data = s.recv(1024) 
        print('Received', repr(data))

