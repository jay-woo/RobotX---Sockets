import socket
import time

"""Creates 3 server sockets"""
serverSocketA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocketB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocketC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""Selects an IP address/port and binds each socket"""
host = socket.gethostname() #For testing purposes
portA = 3232
portB = 4343
portC = 5454

serverSocketA.bind((host, portA))
serverSocketB.bind((host, portB))
serverSocketC.bind((host, portC))

"""Waits until all connections are made and accepts them"""
serverSocketA.listen(5)
serverSocketB.listen(5)
serverSocketC.listen(5)

clientSocketA, addrA = serverSocketA.accept()
clientSocketB, addrB = serverSocketB.accept()
clientSocketC, addrC = serverSocketC.accept()

"""Delivers data to each client
        A - Nav data
        B - LIDAR stream
        C - Image data         """
while True:
    fileA = open('sample1.xml', 'rb').read()
    fileB = open('sample2.xml', 'rb').read()
    fileC = open('sample3.xml', 'rb').read()
        
    clientSocketA.send(fileA.encode('ascii'))
    clientSocketB.send(fileB.encode('ascii'))
    clientSocketC.send(fileC.encode('ascii'))
    
    time.sleep(0.1)