from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DateTimeField, SelectField, TextAreaField, SubmitField, RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    breed = StringField("What breed are you ? ", validators=[DataRequired()])
    tomcat = BooleanField("Have you been tomcat ?")
    mood = RadioField("Please Choose your mood : ", choices = [('mood_one', 'bad'), ('mood_two', 'good')])
    food_choice = SelectField(u'Pick your fav food : ', choices=[('chi','Chicken'), ('bef','Beef'), ('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField("Submit")

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['tomcat'] = form.tomcat.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thankyou'))
    return render_template("home1.html",form = form)
        

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ =='__main__' :
    app.run(debug=True,port=5500)
