import socket


class Socket(socket.socket):
	def __init__(self,ip,port):
		self.ip = ip
		self.port = port
		self.sk = socket.socket()
		self.c = 0
		self.addr = "127.0.0.1"

	def bind(self):
		self.sk.bind((self.ip, self.port))        # Bind to the port

	def listen(self,clients):
		self.sk.listen(clients)                 # Now wait for client connection.

	def accept(self):
		self.c, self.addr = self.sk.accept()     # Establish connection with client.
		print ('Got connection from', self.addr)

	def send(self, msg):
		self.sk.send(msg.encode())

	def sends(self, msg):
		self.c.send(msg.encode())

	def close(self):
		self.c.close()                # Close the connection

	def connect(self):
		self.sk.connect((self.ip, self.port))

	def receive(self):
		return self.c.recv(1024).decode()

	def rece(self):
		return self.sk.recv(1024).decode()
