# Echo client program
"""
Cliente -> Subscriber
"""
import socket

HOST = '127.0.0.1'          # The remote host
PORT = 5050            # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # choice = input()                    # input no console
    # s.sendall(bytes(choice, 'utf-8'))   # transforma string em bytestream

    is_subscriber = b'subscriber'
    s.sendall(is_subscriber)
    topic = input("[INSERT TOPIC NAME] ")
    s.send(bytes(topic, 'utf-8'))
    while True:
        msg = input("[DIGITE UMA MENSAGEM DE TESTE: ]")
        s.send(bytes(msg, 'utf-8'))
        
