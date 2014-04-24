import socket
import time

serverSocketA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocketB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocketC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname() #For testing purposes
portA = 1513
portB = 1616
portC = 1781

serverSocketA.bind((host, portA))
serverSocketB.bind((host, portB))
serverSocketC.bind((host, portC))

serverSocketA.listen(5)
serverSocketB.listen(5)
serverSocketC.listen(5)

while True:
    clientSocketA, addrA = serverSocketA.accept()
    clientSocketB, addrB = serverSocketB.accept()
    clientSocketC, addrC = serverSocketC.accept()
    
    print("Got a connection from %s" % str(addrA))
    print("Got a connection from %s" % str(addrB))
    print("Got a connection from %s" % str(addrC))
    
    currentTime = time.ctime(time.time()) + "\r\n"
    clientSocketA.send(currentTime.encode('ascii'))
    clientSocketB.send(currentTime.encode('ascii'))
    clientSocketC.send(currentTime.encode('ascii'))
    
    serverSocketA.close()
    serverSocketB.close()
    serverSocketC.close()