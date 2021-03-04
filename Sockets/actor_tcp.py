import socket as sck

ip_sender = "127.0.0.0"
port_sender = "7000"

ip_receiver ="127.0.0.0"
port_receiver = "7000"

tupla_sender = (ip_sender, port_sender)
tupla_receiver = (ip_receiver, port_receiver)

#server

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind(tupla_sender)

s.listen()

connessione, ipMittente = s.accept()

data = connessione.recv(4096).decode()

s.close()

#client

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

s.connect(tupla_receiver)

s.sendto(data , tupla_receiver)

s.close()