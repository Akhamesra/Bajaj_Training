from wtforms import Form, BooleanField, StringField, validators, SubmitField, HiddenField
from flask_wtf import FlaskForm

class owner(FlaskForm):
    name = StringField("What is your name ? ")
    pet_name = StringField("Your pet name ? ")
    pet_breed = StringField("What is your pet breed ? ")
    submit = SubmitField("Submit")


