

import socket

server_ip = "localhost"
port = 7000
ack = False
c = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while(1):
    msg = input("inserire un messaggio: ").decode()
    if(msg == "close"):
        break
    while(ack)
        c.sendto(msg.encode(),(server_ip,port))
        data,address = c.recvfrom(4096)
        if(data == None):
            ack = True

c.close()
