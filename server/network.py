import socket
import pickle

bitSize = 2048*2 #increase this number if get pickle data truanced or ran out of input errors

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #### server IPv4 address. Find using ipconfig in Command Prompt. 
        #self.server = "192.168.1.238" #Work computer
        self.server = "192.168.0.25" #Personal laptop
        self.port = 5555
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(bitSize).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(bitSize))
        except socket.error as e:
            print(e)

