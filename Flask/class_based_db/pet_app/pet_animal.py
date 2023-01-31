from wtforms import Form, BooleanField, StringField, validators, SubmitField, HiddenField
from flask_wtf import FlaskForm
from flask import render_template, Flask,redirect,url_for,request
import psycopg2
from form import owner

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' #CSRF token

def get_db_connection():
    conn = psycopg2.connect(host = 'localhost',
                            database = 'Flask_db',
                            user = 'postgres',
                            password = 'Finserv@2023')
    return conn

# db = DBconnection()

@app.route('/')
def index():
    conn = get_db_connection()
    curr = conn.cursor()
    curr.execute('SELECT * FROM pet_shop;')
    pet_shop = curr.fetchall()
    curr.close()
    conn.close()
    return render_template('index.html',pet_shop = pet_shop)

@app.route('/create',methods = ['GET','POST'])
def create():
    form = owner()
    if form.validate_on_submit():
        name = form.name.data
        pet_name = form.pet_name.data
        pet_breed = form.pet_breed.data

    if request.method == 'POST':
            conn = get_db_connection()
            curr = conn.cursor()
            curr.execute('INSERT INTO pet_shop (pet_name, pet_breed, owner)'
                'VALUES (%s, %s, %s)',
                (pet_name,pet_breed,name)
                )
            conn.commit()
            curr.close()
            conn.close()
            return  redirect(url_for('index'))
    return render_template('create.html',form = form)


@app.route('/delete/<int:ids>')
def delete(ids):
    conn = get_db_connection()
    curr = conn.cursor()
    t = (ids,)
    curr.execute('DELETE FROM pet_shop WHERE id = %s', (ids,))
    conn.commit()
    curr.close()
    conn.close()
    return redirect(url_for('index'))


    



if __name__ == '__main__':
    app.run(debug=True, port = 5500)

