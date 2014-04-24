import socket

clientSocketA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocketB = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocketC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
portA = 1513
portB = 1616
portC = 1781

clientSocketA.connect((host, portA))
clientSocketB.connect((host, portB))
clientSocketC.connect((host, portC))

tmA = clientSocketA.recv(1024)
tmB = clientSocketB.recv(1024)
tmC = clientSocketC.recv(1024)

clientSocketA.close()
clientSocketB.close()
clientSocketC.close()

print("The time got from the server is %s" % tmA.decode('ascii'))
print("The time got from the server is %s" % tmB.decode('ascii'))
print("The time got from the server is %s" % tmC.decode('ascii'))