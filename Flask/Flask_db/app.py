import os
import psycopg2
from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host = 'localhost',
                            database = 'Flask_db',
                            user = 'postgres',
                            password = 'Finserv@2023')

    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    curr = conn.cursor()
    curr.execute('SELECT * FROM Books;')
    books = curr.fetchall()
    curr.close()
    conn.close()
    return render_template('index.html',books=books)

@app.route('/create', methods = ['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        pages_num = int(request.form['pages_num'])
        review = request.form['review']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO books (title, author, pages_num, review)'
                    'VALUES (%s, %s, %s, %s)',
                    (title, author, pages_num, review))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/delete/<int:ids>')
def delete(ids):
    conn = get_db_connection()
    curr = conn.cursor()
    t = (ids,)
    curr.execute('DELETE FROM books WHERE id = %s', (ids,))
    conn.commit()
    curr.close()
    conn.close()
    return redirect(url_for('index'))


    



if __name__ == '__main__':
    app.run(debug=True, port = 5500)

