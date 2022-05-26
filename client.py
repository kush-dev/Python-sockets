from socket import*

serverName='localhost'
serverPort=1234
clientSocket=socket(AF_INET,SOCK_DGRAM)
print('Connected')
message=input("Enter message:...")
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage ,serverAddress=clientSocket.recvfrom(123)
print('Message Received')
print("From server:",modifiedMessage.decode(),serverAddress)
clientSocket.close()