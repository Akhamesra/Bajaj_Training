from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, SelectField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class SimpleForm(FlaskForm):
    submit = SubmitField('Click Me')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        flash("You Just clicked the button")
        flash("Once More")
        return redirect(url_for('index'))
    return render_template("home2.html",form = form)

if __name__ =='__main__':
    app.run(debug=True,port=5500)
