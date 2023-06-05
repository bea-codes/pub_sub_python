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
	
	client_and_topic = [conn]
	# print(f"client and topic 1 {client_and_topic}\n")

	isSubscriberStream = conn.recv(1024)
	isSubscriber = isSubscriberStream
	topic = None
	first_msg = b''

	if isSubscriber == b'subscriber':
		client_and_topic.append('subscriber')
		topic_stream = conn.recv(1024)
		topic = topic_stream
		if any(topic in t[0] for t in topics):
			pass
		else:
			topics.append([topic, first_msg])

		
	elif isSubscriber == b'publisher':
		client_and_topic.append('publisher')
		topic_stream = conn.recv(1024)
		topic = topic_stream
		first_msg_stream = conn.recv(1024)
		first_msg = first_msg_stream
		if any(topic in t[0] for t in topics):
			pass
		else:
			topics.append([topic, first_msg])
	
	# print(f"client and topic 2 {client_and_topic}")

	client_and_topic.append(topic)
	# print(f"client and topic 3 {client_and_topic}") -> isso foi só pra testar o valor da variável durante a execução e tals

	if client_and_topic[1] == 'subscriber':
		subscribers.append(client_and_topic)
		print(f"[{addr}] added to list of subscribers")
	elif client_and_topic[1] == 'publisher':
		publishers.append(client_and_topic)		
		print(f"[{addr}] added to list of publishers")


	# print(f"TODOS OS TÓPICOS: {topics}")

	if client_and_topic[1] == 'subscriber':
			for t in topics:
				if t[0] == client_and_topic[2]:
					last_msg = t[1]
					conn.sendall(last_msg)
	
	while True:
		data = conn.recv(1024)

		if client_and_topic[1] == 'publisher':
			for t in topics:
				if t[0] == client_and_topic[2]:
					if data != b'':
						t[1] = data
					# print(f"TOPICO {t[0]} ULTIMA MENSAGEM {t[1]} ")

			for sub in subscribers:
				sub_connection = sub[0]
				sub_topic = sub[2]
				if sub_topic == client_and_topic[2]:
					sub_connection.sendall(b'[MESSAGE RECIEVED FROM PUBLISHER] ' + data)
		

		if not data: return
		print(f"[MESSAGE RECIEVED FROM {addr}] {data}")
		# print(topics)
	


start_server()