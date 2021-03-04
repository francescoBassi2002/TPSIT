import socket


ip = "localhost"
port = 7000

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((ip,port))
while(1):
    msg,address = s.recvfrom(4096)
    if(msg.decode() == "close"):
        break
    print(msg.decode())
    #ack
    s.sendto(msg, (ip, port) )

s.close()