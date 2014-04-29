import socket
import time

"""Creates 1 server socket"""
serverSocketD = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""Selects an IP address/port and binds each socket"""
host = socket.gethostname() #For testing purposes
portD = 1414

serverSocketD.bind((host, portD))

"""Waits until all connections are made and accepts them"""
serverSocketD.listen(5)

clientSocketD, addrD = serverSocketD.accept()

"""Delivers data to each client
        D - Var client         """
while True:
    fileD = open('sample4.xml', 'rb').read()
        
    clientSocketD.send(fileD.encode('ascii'))
    
    time.sleep(0.1)