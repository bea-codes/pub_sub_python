# Echo client program
"""
Cliente -> Subscriber
"""
import socket

HOST = '127.0.0.1'          # The remote host
PORT = 5050            # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    is_subscriber = b'subscriber'
    s.sendall(is_subscriber)
    topic = input("[INSERT TOPIC NAME] ")
    s.send(bytes(topic, 'utf-8'))
    while True:
        data = s.recv(1024)
        print(bytes(data))
