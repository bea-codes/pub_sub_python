"""
Servidor do sistema Publisher/Subscriber 
Projeto para disciplina de Redes de Computadores - Sistemas para Internet, UNICAP

"""

import socket
import threading

HOST = '127.0.0.1'
PORT = 5050

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# Armazena informações dos clientes
publishers = []
subscribers = []
topics = []


def start_server():
	server.listen(5)
	with server:
		while True:			
			active_threads = threading.active_count()
			conn, addr = server.accept()
			if active_threads < 7:
				thread = threading.Thread(target=handle_client, args=(conn, addr))
				thread.start()
				print(f"[ACTIVE NUMBER OF THREADS {active_threads - 1}]")
			else:
				print(f"[NUMBER OF ACCEPTED THREADS EXCEEDED] {active_threads} threads active.")
				conn.send(b"[SERVER CANNOT ACCEPT MESSAGES FROM YOUR DEVICE]")
				conn.close()


def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	
	client_and_topic = [addr]
	print(f"client and topic 1 {client_and_topic}\n")

	isSubscriberStream = conn.recv(1024)
	isSubscriber = isSubscriberStream

	if isSubscriber == b'subscriber':
		client_and_topic.append('subscriber')
		print(f"[{addr}] added to list of subscribers")
	elif isSubscriber == b'publisher':
		client_and_topic.append('publisher')
		print(f"[{addr}] added to list of publishers")
	
	print(f"client and topic 2 {client_and_topic}")


		
	topic = conn.recv(1024)
	topics.append([topic])
	client_and_topic.append(topic)
	print(f"client and topic 3 {client_and_topic}")

	if client_and_topic[1] == 'subscriber':
		subscribers.append(client_and_topic)
	elif client_and_topic[1] == 'publisher':
		publishers.append(client_and_topic)		

	print(f"=================\n[SUBSCRIBERS] {subscribers}")
	print(f"=================\n[PUBLISHERS] {publishers}")

	while True:
		data = conn.recv(1024)
		if not data: return
		print(f"[MESSAGE RECIEVED FROM {addr}] {data}")
	







start_server()

