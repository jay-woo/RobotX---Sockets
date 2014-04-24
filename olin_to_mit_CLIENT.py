import socket

"""Number of bits to be transferred"""
fileSize = 1024

"""Sets up sockets for each client to receive data"""
clientSocketA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocketB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocketC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
portA = 3232
portB = 4343
portC = 5454

clientSocketA.connect((host, portA))
clientSocketB.connect((host, portB))
clientSocketC.connect((host, portC))

"""Each socket receives data from the server"""
while True:
    dataA = clientSocketA.recv(fileSize)
    dataB = clientSocketB.recv(fileSize)
    dataC = clientSocketC.recv(fileSize)
    
    print("Data A: %s" % dataA.decode('ascii'))
    print("Data B: %s" % dataB.decode('ascii'))
    print("Data C: %s" % dataC.decode('ascii'))