import socket as sck

ip = 'localhost'
porta=6300

client = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

client.connect((ip,porta))

while(1):
    dato = input("messaggio: ")
    if(dato=='close'):
        break
    client.sendall(dato.encode())

    messaggio = client.recv(4096).decode()
    if(not (messaggio == None)):
        print(f"rislutato: {messaggio}")

client.close()
    