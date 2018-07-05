import tcpsocket as tp

def Main():
	s = tp.Socket("127.0.0.1",12345)
	s.connect()
	msg = input("Girl:")
	while True:
		s.send(msg)
		print("Boy:",s.rece())
		msg = input("Girl:")
	s.close()
		


if __name__ == '__main__':
	Main()
