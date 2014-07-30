import socket

class StockzClient():
	
	def __init__(self, address = ('127.0.0.1', 1337)):
		if not isinstance(address, tuple):
			raise TypeError('address must be a tuple')

		if not len(address) == 2:
			raise TypeError('address must be a tuple (str, int)')

		if not isinstance(address[0], basestring) or not isinstance(address[1], int):
			raise TypeError('address must be a tuple (str, int)')

		self._address = address
			
	def execute(self, data, timeout = 5):
		if not isinstance(data, basestring):
			raise TypeError('data must be a string')

		if not isinstance(timeout, int):
			raise TypeError('timeout must be an int')

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect(self._address)
		sock.settimeout(timeout)

		sock.sendall(data)

		response = sock.recv(2048)

		sock.close()

		if not isinstance(response, basestring):
			return None

		return response