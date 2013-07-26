#!/usr/bin/env python

import SocketServer

class EchoHander(SocketServer.BaseRequestHandler):
	def handle(self):
		print 'Got connection from : ', self.client_address
		data = 'dummy'
		while len(data):
			data = self.request.recv(1024)
			print 'data sent ==> %s' %data
			self.request.send(data)
		print 'Client %s left'%self.client_address
		




serverAddr = ("0.0.0.0", 50003)
server = SocketServer.TCPServer(serverAddr, EchoHander)
server.serve_forever() 