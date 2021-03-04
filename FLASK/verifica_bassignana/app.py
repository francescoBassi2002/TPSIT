import semaforo
from flask import render_template , Flask , request, url_for,redirect
import time
import datetime as dt
import sqlite3 as sq
from sqlite3 import Error
import pymongo as mb


app = Flask(__name__)

s = semaforo.semaforo()

stato_s = True #true se il semaforo è acceso e false se spento, di default è true

tempo_giallo = 0
tempo_rosso = 0
tempo_verde=0

def carica_database(stato_s): # funzione che carica nel database lo stato del semaforo (se stato acceso o spento) e data e ora in cui è cambiato

    stringa = ""
    
    if stato_s:
        stringa = "acceso"
    else:
        stringa = "spento"

    #aggiungo la riga al database
    
    client = mb.MongoClient("mongodb://localhost:27017/")    
    conn = client["database_semaforo"]
    mycol = conn["azioni_semafori"]
    data = {"stato" : stringa , "ora" : str(dt.datetime.now())}
    mycol.insert_one(data)



    """
    try:
        conn = sq.connect('database.db')
        cursor = conn.cursor()
        print(f"INSERT INTO semafori (azione,data_ora) values ('{stringa}','{str(dt.datetime.now())}')")
        cursor.execute(f"INSERT INTO semafori (azione,data_ora) values ('{stringa}','{str(dt.datetime.now())}')")
        conn.commit() #per salvare le modifiche
        conn.close()
    except Error as E:
        print(E)
    """
#pagina di configurazione
@app.route('/', methods=['POST','GET'])
def config():
    global tempo_giallo, tempo_verde, tempo_rosso, stato_s
    tempo_giallo = 0
    tempo_rosso = 0
    tempo_verde=0
    stato_s = True
    

    if request.method == 'POST':
        if request.form['t_v']=="":
            tempo_verde == 0
        else:
            tempo_verde = int(request.form['t_v'])

        if request.form['t_g']=="":    
            tempo_giallo == 0
        else:
            tempo_giallo = int(request.form['t_g'])

        if request.form['t_r']=="":
            tempo_rosso = 0
        else:
            tempo_rosso = int(request.form['t_r'])


        if request.form['btn'] == "attiva": #assegna a stato_s True se si decide di attivare il semaforo, False per il contrario
            stato_s = True
        else:
            stato_s = False

        return redirect('/elaborazione')


        
    

    return render_template('gestione_semaforo.html')


#funziona che apre la pagina non appena finisce di essere elaborato il processo utilizzando i dati della configurazione
@app.route('/elaborazione',methods=['POST','GET'])
def test():
    
    carica_database(stato_s) #funzione per database, vedi riga 18

    if stato_s: #funzione in caso di semaforo acceso
      
    
        s.rosso(tempo_rosso)
        s.verde(tempo_verde)
        s.giallo(tempo_giallo)
            
    else: #azione in caso di semaforo spento
        
        for _ in range(3):
            s.giallo(tempo_giallo)
            s.luci_spente(1)
            
    return "<h1>Elaborazione conclusa</h1>"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')