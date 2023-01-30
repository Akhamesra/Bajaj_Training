from wtforms import Form, BooleanField, StringField, validators, SubmitField, HiddenField
from flask_wtf import FlaskForm
from flask import render_template, Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' #CSRF token

class testForm(FlaskForm):
    cat_breed = StringField("What is your cat breed")
    submit = SubmitField("Submit")

@app.route("/", methods=['POST', 'GET'])
def index():
    cat_breed = False
    form  = testForm()
    if form.validate_on_submit():
        cat_breed = form.cat_breed.data
    return render_template('index.html',form = form, cat_breed = cat_breed)

if __name__ == '__main__':
    app.run(debug=True, port=5500)