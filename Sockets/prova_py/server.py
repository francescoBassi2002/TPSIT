import socket as sck
ip = 'localhost'
port = 6300

server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

server.bind((ip,port))

server.listen()

conn,add = server.accept()

while(1):
    immagine = conn.recv(4096).decode()
    
