import sqlite3
from hashids import Hashids
import string
from random import choice 
import string
from flask import Flask, render_template, request, flash, redirect, url_for
app = Flask(__name__)

d = {}

def generate_short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        url = request.form['url']
        surl = generate_short_id(5)
        d[surl] = url
        #return f"surl : {surl} <br> url : {url} <br> {d}"
        return render_template('index.html', short_url=request.host_url + surl)
    return render_template('index.html')
@app.route('/<id>')
def url_redirect(id):
    original_id = d[id]
    return redirect(original_id)
if __name__ == '__main__':  
   app.run(debug = True)