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
publishers = {}
subscribers = {}


def start_server():
	server.listen(5)
	with server:
		while True:			
			active_threads = threading.active_count()
			conn, addr = server.accept()
			if active_threads < 7:
				thread = threading.Thread(target=handle_client, args=(conn, addr))
				thread.start()
				print(f"[ACTIVE NUMBER OF THREADS {active_threads}]")
			else:
				print(f"[NUMBER OF ACCEPTED THREADS EXCEEDED] {active_threads} threads active.")
				conn.send(b"[SERVER CANNOT ACCEPT MESSAGES FROM YOUR DEVICE]")
				conn.close()


def handle_client(conn, addr):
	print(f"[NEW CONNECTION] {addr} connected.")
	connected = True
	
	
	while connected:
		data = conn.recv(1024)
		# conn.send(b"[SELECT TOPIC] \n 1, 2, 3 OR 4")
		if not data: return
		print(f"Mensagem recebido do cliente {data}")
	
	# conn.send(b"[CONNECT TO SERVER]")
	# while connected:
	# 	# msg = conn.recv(1024)
	# 	# print(msg) 						# Número de bytes aceitáveis podem mudar no futuro







start_server()

""" Passo 1: Definir o protocolo de comunicação
Antes de começar a implementação, é importante definir o protocolo de comunicação que será utilizado entre o servidor e os clientes. O protocolo pode ser simples, como mensagens de texto em formato específico, ou pode ser um formato mais complexo, como mensagens em JSON. Certifique-se de ter uma estrutura clara para a troca de informações entre as partes.

Passo 2: Implementar o servidor
O servidor central será responsável por receber as mensagens dos publicadores e distribuí-las para os assinantes. Ele também deverá armazenar as últimas mensagens de cada tópico, mesmo que os clientes tenham se desconectado. Aqui estão os passos básicos para implementar o servidor:

a) Criar um socket do tipo TCP/IP e vinculá-lo a um endereço IP e número de porta específicos.
b) Aguardar conexões dos clientes.
c) Quando um cliente se conectar, receber sua mensagem de inicialização, que deve incluir o tipo (publisher ou subscriber) e o tópico de interesse.
d) Armazenar o cliente em uma lista ou estrutura de dados adequada, de acordo com seu tipo e tópico.
e) Distribuir mensagens dos publicadores para os assinantes corretos.
f) Enviar a última mensagem armazenada em um tópico para novos assinantes que se inscreverem no mesmo.
g) Lidar com desconexões de clientes de forma adequada, removendo-os da lista de clientes ativos.

Passo 3: Implementar o cliente publicador
O cliente publicador será responsável por se conectar ao servidor e enviar mensagens para um determinado tópico. Aqui estão os passos básicos para implementar o cliente publicador:

a) Criar um socket do tipo TCP/IP.
b) Conectar-se ao servidor utilizando o endereço IP e número de porta corretos.
c) Enviar uma mensagem de inicialização para o servidor, indicando que é um publicador e o tópico de interesse.
d) Aguardar a entrada do usuário ou outra fonte de mensagens.
e) Enviar as mensagens ao servidor, juntamente com o tópico correspondente.
f) Lidar com desconexões de forma adequada, encerrando a conexão corretamente.

Passo 4: Implementar o cliente assinante
O cliente assinante será responsável por se conectar ao servidor e receber mensagens de um determinado tópico. Aqui estão os passos básicos para implementar o cliente assinante:

a) Criar um socket do tipo TCP/IP.
b) Conectar-se ao servidor utilizando o endereço IP e número de porta corretos.
c) Enviar uma mensagem de inicialização para o servidor, indicando que é um assinante e o tópico de interesse.
d) Aguardar a recepção de mensagens do servidor.
e) Lidar com desconexões de forma adequada, encerrando a conexão corretamente.

Passo 5: Testar a comunicação entre os clientes e o servidor
Após implementar o servidor, o cliente publicador e o cliente assinante, você pode testar a comunicação entre eles para garantir """