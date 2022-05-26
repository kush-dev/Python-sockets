import socket;

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((socket.gethostname(),12345))

msg=s.recv(1024) # //number of bytes one should be able to receive from the SOCK_STREAM//

print(msg.decode("utf-8"))
s.close()

