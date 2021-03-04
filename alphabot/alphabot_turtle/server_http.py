from flask import Flask, jsonify, request

import sqlite3 as sq
import logging


app = Flask(__name__)

logging.basicConfig(filename='example.log', level=logging.DEBUG)

def checkParams(dizionario):
    if ('arrivo' in dizionario) and ('partenza' in dizionario):
        return True 
    else:
        return False

def percorsoDb(inizio,fine):
    try:
        database = sq.connect('percorsi.db', 5.0, 0, None, False)
        cursore = database.cursor()
    except Exception as error:
        print(f"database error: {error}")


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
    
        return "not found"
               
    else:

        for a in lista_tuple:       
            print(a) #è una tupla, mi serve solo il primo elemento che è la stringa
            informazione = a
        
        return informazione[0]
               
        
       

    


@app.route('/api/percorso', methods = ['GET'])
def api_percorso():
    
    if request.method == 'GET':
        if checkParams(request.args):
            arrivo = int(request.args['arrivo'])
            partenza = int(request.args['partenza'])


            percorso = percorsoDb(partenza,arrivo)

            if (percorso == "not found"):
                return "Percorso inesistente"
            else:

                return jsonify({"percorso" : percorso}) 
        else:
            return "url non valido, bisogna inserire una partenza e un arrivo"


if __name__ == "__main__":
    app.run(host = '127.0.0.1' , debug = True)