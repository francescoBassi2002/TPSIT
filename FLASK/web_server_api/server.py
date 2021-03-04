from flask import Flask,jsonify,redirect,url_for, request
import pymongo
import sqlite3 as sq

app = Flask(__name__)

books = [{'id':0,
        'title' : 'Il nome della Rosa',
        'author' : 'Umberto Eco',
        'year_published' : '1980'},
        {'id':1,
        'title' : 'Il problema dei tre corpi',
        'author' : 'Liu Cixin',
        'year_published' : '2008'},
        {'id':2,
        'title' : 'Fondazione',
        'author' : 'Isaac Asimov',
        'year_published' : '1951'}
        ]

def verifica(id):
    conn = sq.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM libri WHERE id = {id}")
    rs = cursor.fetchone()
    dc = {"id" : rs[0] , "title" : rs[1] , "author" : rs[2] , "year_published" : rs[3]}
    return dc

@app.route('/api/cerca_libro', methods=['GET'])
def api_libri():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error, url is invalid"
    
    """result = []
    for book in books:
        if book['id'] == id:
            result.append(book)"""

    dictionary = verifica(id)

    return jsonify(dictionary)




if __name__ == "__main__":
    app.run(host = '127.0.0.1', debug =True)