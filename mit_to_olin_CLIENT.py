import socket

"""Number of bits to be transferred"""
fileSize = 1024

"""Sets up sockets for each client to receive data"""
clientSocketD = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
portD = 1414

clientSocketD.connect((host, portD))

"""Each socket receives data from the server"""
while True:
    dataD = clientSocketD.recv(fileSize)
    
    print("Data D: %s" % dataD.decode('ascii'))