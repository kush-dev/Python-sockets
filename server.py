from socket import*

serverPort=1234
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print('Connection Established!')
print('Server is in waiting....')

while True:
 	message,clientAdress=serverSocket.recvfrom(123)
 	print(message.decode(),clientAdress)
 	modifiedMessage=message.upper()

 	serverSocket.sendto(modifiedMessage,clientAdress)
 	serverSocket.close()


 	

 	

