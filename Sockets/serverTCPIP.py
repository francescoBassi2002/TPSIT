import socket as sck

ip = 'localhost'
port = 6200 
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
tupla = (ip,port)
s.bind(tupla)
s.listen()
print("in ascolto")
connessione, ip_mittente = s.accept()
print(f"connessione con {ip_mittente}")
while(True):
   
    data = connessione.recv(4096).decode()
    if(data == "close"):
        break
    print(f"dato: {data}")
    connessione.sendto(data.encode(), tupla)
s.close()