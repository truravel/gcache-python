import socket
import sys


class GCache:
    host = 'localhost'
    port = 3990
    server_address = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_TCP)

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def getval(self, key):
        return 0

    def setval(self,key,value):
        self.send( """SET %s %s""" % (key,value) )
        return 0

    def delete(self, key):
        return 0

    def connect(self):
        self.server_address = (self.host, self.port)
        self.sock.connect(self.server_address)

    def send(self,value):
        data = self.sock.send(value)
        resp = self.sock.recv(2048)
        if resp != 'OK':
            print(resp)

    def receive(self):
        data = self.sock.recv(2048)
        return

    def close(self):
        self.sock.close()

