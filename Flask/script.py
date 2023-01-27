from flask import *
from random import choice 
import string
app = Flask(__name__)  
 
@app.route('/')
def home():
    return "<a href='http://127.0.0.1:5000/index'>Index</a> <a href='http://127.0.0.1:5000/info'>Info</a><a href ='http://127.0.0.1:5000/urlshortner'>urlshortner</a> <br><h1>Welcome to my website</h1>"

@app.route('/index')  
def index():  
      return render_template('index.html',Myname = "Akshit")  

@app.route('/info')
def info():
    browser_info = request.headers.get('User-Agent')
    return f'<h2>Info : {browser_info}</h2>'

def generate_short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))
@app.route('/urlshortner/<url>')
def urlshortner(url):
    surl = generate_short_id(6)
    surl += ".com"
    return render_template('urlshortner.html', surl)
    

if __name__ == '__main__':  
   app.run(debug = True)