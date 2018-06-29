import socket


class Socket(socket.socket):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port

    def create():
        return self.socket.socket()         # Create a socket object

    def bind():
        self.socket.bind((self.ip, self.port))        # Bind to the port

    def listen(clients):
        self.socket.listen(client)                 # Now wait for client connection.

    def accept():
        c, addr = self.socket.accept()     # Establish connection with client.
         #print ('Got connection from', addr)

    def send():
        c.send('Thank you for connecting')

    def close():
        c.close()                # Close the connection



def Main():
    s = Socket("127.0.0.1","12345")
    s.bind()
    s.listen(5)
    while True:
        s.accept()


if __name__ == '__main__':
    Main()