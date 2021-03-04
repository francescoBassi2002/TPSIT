import threading
import socket as sck

class ClientThread (threading.Thread):
    def __init__(self,connessione,tupla):
       threading.Thread.__init__(self)
       self.connessione = connessione
       self.tupla = tupla


    def run(self):
        while(1):
            data = self.connessione.recv(4096).decode()
            print(f"dato: {data} ricevuto da {self.tupla}")
            if (data == "close"):
                break
            self.connessione.sendall(data.encode())





ip = 'localhost'
port = 6300
threads = []
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)

s.bind((ip,port))
s.listen()

while(1):
    connessione,indirizzo = s.accept()
    
    threads.append(ClientThread(connessione, indirizzo))
    threads[len(threads)-1].start()


