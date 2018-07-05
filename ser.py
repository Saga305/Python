import tcpsocket as tp

def Main():
	s = tp.Socket("127.0.0.1",12345)
	s.bind()
	s.listen(5)
	s.accept()
	while True:
		print("Girl:",s.receive())
		msg = input("Boy:")
		s.sends(msg)
	s.close()


if __name__ == '__main__':
	Main()
