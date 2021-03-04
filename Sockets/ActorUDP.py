"""
ACTOR UDP - RIPETITORE
"""
import socket

"""
VARIABLE DATA
"""

receiver_ip = "192.168.0.126"   #dati dell'host da cui ricevo il messaggio
receiver_port = 7000

sender_ip = "192.168.0.131"     #dati dell'host a cui invio il messaggio
sender_port = 7000

"""
SERVER
"""

#creazione del socket
s= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#bind del server per esporlo sulla rete
s.bind((receiver_ip, receiver_port))

#funzionamento (legge il messaggio e lo restituisce)
data, address = s.recvfrom(4096)
print (data.decode())

#chiusura del socket
s.close()

"""
CLIENT
"""

#creazione del socket
s= socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#funzionamento (legge il messaggio e lo invia al server)
server_address=(sender_ip,sender_port)
s.sendto(data, server_address)

#chiusura del socket
s.close()
