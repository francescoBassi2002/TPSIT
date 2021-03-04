from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def validate(username,passowrd):
    cond = True
    conn_db = sqlite3.connect('database.db')
    cursore = conn_db.cursor()
    cursore.execute(f"SELECT * FROM credenziali WHERE psw = '{passowrd}' AND username = '{username}' ")
    lista_tuple = cursore.fetchall()
    conn_db.close()
    if len(lista_tuple) == 0: #non ha trovato niente
        cond = False
    else:
        cond = True

    return cond

@app.route('/log' , methods=['GET','POST'])
def login():
    error = None
    print(request.headers)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        
        print(f"{password} , {username}")
        completion =validate(username,password) #ritorna true se si ha inserito qualcosa oppure ritorna errore
        if completion == False:

            error = 'invalid credentials. please try again'

        else: 


            return redirect(url_for('secret'))

    return render_template('index.html' , error=error)


@app.route('api/controlla/<value>' , methods=['GET','POST'])
def controllo(): 










@app.route('/secret')
def secret():
    return "This is a secret page"

   
if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)