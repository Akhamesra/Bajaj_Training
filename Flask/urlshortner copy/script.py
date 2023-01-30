import sqlite3
from hashids import Hashids
import string
from random import choice 
import string
from flask import Flask, render_template, request, flash, redirect, url_for, render 
app = Flask(__name__)

d = {}

def generate_short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))

@app.route('/urlshort/<url>')
def index(url):
    surl = generate_short_id(5)
    d[surl] = url
    return request.host_url + surl

@app.route('/<id>')
def url_redirect(id):
    #original_url = d[id]
    context = {}
    return render(request,d[id],context)
    #return redirect(d[id])
if __name__ == '__main__':  
   app.run(debug = True)