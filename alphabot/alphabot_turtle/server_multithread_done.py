"""

!! non gestisci gli errori quando il server si disconette 
!! se inserisco un valore sbagliato(from,to) non mi fa continuare 
!! non michiare gli spazi con i TAB



!!il tuo problema principale è che le turtle hanno dei problemi ad aprire  una seconda finestra nella stessa esecuzione del programma
Perciò o riavvii il programma o gestisci l'errore come ho fatto io:

1)nel modulo [my_turtle] ho sostituito "wn.oneclick()" con "wn.mainloop"
2)alla fine di
"""
import threading 
import specifiche
import turtle
import logging
import socket as sck
import sqlite3 as sq
logging.basicConfig(filename='example.log', level=logging.DEBUG)

ack ="ack"

messaggio_errore_senza_percorso = "spiacente, non ci sono percorsi disponibili per le due destinazioni"
nomeImmagineServer = "imgServer.jpg"

try:
    database = sq.connect('percorsi.db', 5.0, 0, None, False)
    cursore = database.cursor()
except Exception as error:
    print(f"database error: {error}")



threads = []
ip = 'localhost'
port = 6300
tupla = (ip,port)
server = sck.socket(sck.AF_INET, sck.SOCK_STREAM)


def percorso(conn, tupla, cursore, fine, inizio):
    logging.debug(" server : entrato in funzione percorso")
     
     
     #print e debug------------------------------------------------------------------------------------------------
    print(f"client: {tupla}")
    print(f"inizio: {inizio}, fine: {fine}")
   
    logging.debug(f" server : Istruzione: SELECT percorso FROM percorsi INNER JOIN inizio_fine ON inizio_fine.id_percorso = percorsi.id WHERE (id_start = {inizio}) AND (id_end = {fine})")
     #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    try :
        #eseguo la query e metto le tuple in una lista------------------------------------------------------------------------------------------------------------------------
        cursore.execute(f"SELECT percorso FROM percorsi INNER JOIN inizio_fine ON inizio_fine.id_percorso = percorsi.id WHERE (id_start = {inizio}) AND (id_end = {fine})")
        lista_tuple = cursore.fetchall()
        #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    except Exception as errordb:
         print(f"error database: {errordb}")
    
    if(len(lista_tuple)==0):
        try:
            logging.debug("server : 1.1 : percorso non trovato")
            conn.sendto(messaggio_errore_senza_percorso.encode(), tupla) #1) nomi troppo lungo per una variabile 2)stai mischiando TCP e UDP
            logging.debug(" server : invio messaggio percorso non trovato")
            print(conn.recv(4096).decode()) #ack
            logging.debug(" server : client ha ricevuto messaggio percorso non trovato")
        except Exception as errorSocket:
            print(f"error Socket :{ errorSocket}")
            return          
    else:

        for a in lista_tuple:       
            print(a) #è una tupla, mi serve solo il primo elemento che è la stringa
            informazione = a
        try: 
            conn.sendto(informazione[0].encode(), tupla)
            logging.debug(f"server : 0.0 : percorso inviato {informazione[0]}")
            print(conn.recv(4096).decode()) #ack
            logging.debug("server : client ha ricevuto il percorso")
        except Exception as errorSocket:
            print(f"error Socket :{errorSocket}")
            return          
        
    informazione = None     


    
def ricevi_img(conn,tupla):
     print("ricezione immagine...")

     ricezione_img = "got image"
     
     
     #ricezione immagine
     myfile = open(nomeImmagineServer,'wb')
     
     
 
     while(1):
         messaggio = conn.recv(4096)
         conn.sendall(ack.encode())
         if(messaggio == "ENDIMG".encode()):
             break
         myfile.write(messaggio)
         messaggio = None
 
     logging.debug(" server : 0.1 : image sending: succesful")
     print("immagine ricevuta")
     #ack
     conn.sendto(ricezione_img.encode(),tupla)
     print(conn.recv(4096))
     myfile.close()
 
 
 

class ClientThread (threading.Thread):
    def __init__(self,connessione,tupla):
       threading.Thread.__init__(self)
       self.conn = connessione
       self.tupla_mittente = tupla

    def run(self):       
        print(f"numero client: {specifiche.n_client}")
        while(1):
            try:
                
                data = self.conn.recv(4096)
                #logging.debug(" server : ho ricevuto il dato iniziale")
                self.conn.sendall(f"ack : {data.decode()}".encode())
                #logging.debug(f"messaggio: {data}") #start
                
            except Exception as error:
                print(f"error recv: {error}")
                break
                
            if(not (data.decode().find('close') == -1)):
                    break

            elif(data.decode() == "STARTIMG"):
                
                ricevi_img(self.conn,self.tupla_mittente)         
               
                            

            else:    
                try:
                    percorso(self.conn, self.tupla_mittente, cursore, data.decode().split(',')[0], data.decode().split(',')[1]) #funzione percorso
                except Exception as error:
                    print(f"error percorso : {error}")

        print(f"Il client {self.tupla_mittente} ha abbandonato")
        
        specifiche.n_client = specifiche.n_client - 1
        if(specifiche.n_client == 0):
            server.close()
        



def main():
    server.bind(tupla)
    server.listen()

    while(1):
        conn, tupla_mittente = server.accept()
        specifiche.n_client = specifiche.n_client + 1
        threads.append(ClientThread(conn,tupla_mittente))
        threads[len(threads)-1].start()
        print(f"numero client: {specifiche.n_client}")
        if(specifiche.n_client == 0):
            break
    
if __name__ == "__main__":
    main()