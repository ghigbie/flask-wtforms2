from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, SelectField
                     RadioField, TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
title = 'Flask WTForms - More Practice'

class InfoForm(FlaskForm):
    breed = StringField('What breed our you?', validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("Please choose your mood:",
                      choices=[('mood_one', 'Happy'), ('mood_two', 'Excited'), ('mood_three', 'Sleepy')])
    food_choice = SelectField(u"Pick your favorite food: ",
                              choices=[('chi', 'Chicken'), ('bf', 'Beef'), ('pk', 'Pork'), ('fish', 'Fish') ])