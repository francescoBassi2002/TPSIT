from flask import *
import sqlite3 as sq
from sqlite3 import Error
import pymongo as mongo
app = Flask(__name__)

client = mongo.MongoClient("mongodb://localhost:27017/")
db = client["database_login"]
tab = db["users"]

def verifica(username, password):

    risultato = tab.find_one({"username" : username , "password" : password})
    if risultato:
        return True
    else:
        return False


    """
    conn = sq.connect('database.db')
    cursore = conn.cursor()
    #print(f"SELECT * FROM utenti WHERE username == '{username}' AND password == '{password}'")
    cursore.execute(f"SELECT * FROM utenti WHERE username = '{username}' and password = '{password}'")
    
    lista_tuple = cursore.fetchall()
    conn.close()
    if(len(lista_tuple) == 0):
        return False
    else:
        return True
    """
    
def verifica_user(username):

    risultato = tab.find_one({"username" : username})
    if risultato:
        return True
    else:
        return False

    """
    conn = sq.connect('database.db')
    cursore = conn.cursor()
    #print(f"SELECT * FROM utenti WHERE username == '{username}' AND password == '{password}'")
    cursore.execute(f"SELECT * FROM utenti WHERE username = '{username}'")
    
    lista_tuple = cursore.fetchall()
    conn.close()
    if(len(lista_tuple) == 0):
        return False
    else:
        return True
    """


def registra(username, password):

    tab.insert_one({"username" : username , "password" : password})

    """conn = sq.connect('database.db')
    cursore = conn.cursor()
    print(f"INSERT INTO utenti (username,password) VALUES ('{username}','{password}') ")
    try:
        cursore.execute(f"INSERT INTO utenti (username,password) VALUES ('{username}','{password}') ")
        conn.commit()
    except Error as Er:
        print(Er)
    conn.close()"""

@app.route('/registrazione', methods=['GET' , 'POST'])
def registrati():
    errore=""
    if request.method == 'POST':
        
        user = request.get_json(force =True)['user']
        psw = request.get_json(force =True)['psw']
        psw1 = request.get_json(force =True)['psw1']
        if psw == psw1 : 
            if verifica(user,psw):
                return "ESISTE"
            else:
                registra(user,psw)
                return "OK"
        else:
            return "PSW NOT EQUAL"
                
    

    return render_template('registrazione.html',error=errore)

@app.route('/form', methods=['GET','POST'])
def main():
   # errore=""

   # if request.method == 'POST':
        
        
    #    user = request.form['pluto']
    #    password = request.form['pippo']
        
    #    if(verifica(user,password)):
    #        return redirect("/paginasegreta")
    #    else:
    #        return "NOT OK"

    return render_template('form.html')



@app.route('/paginasegreta' , methods=['GET'])
def secret():
    return "<h1>This is a secret page</h1>"


@app.route('/api/controllo_user', methods=['POST'])
def controllo():
    data = request.get_json(force =True)
    print(data)
    if request.method == 'POST':
       
        username = request.get_json(force =True)["valore"]
        print(username)
        if verifica_user(username):
            return "OK"
        else:
            return "NOT OK"

@app.route('/api/controllo_tot', methods=['POST'])
def controllo_tot():
    data = request.get_json(force =True)
    print(data)
    if request.method == 'POST':
             
        user = request.get_json(force = True)["username"]
        password = request.get_json(force = True)["password"]

        if verifica(user,password):
            return redirect("/paginasegreta")
        else:
            return "NOT OK"

if __name__ == "__main__":
    app.run(host="127.0.0.1" , debug = True)
    