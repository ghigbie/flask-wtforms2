from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, SelectField,
                     RadioField, TextField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'
title = 'Flask WTForms'

class InfoForm(FlaskForm):
    breed = StringField('What breed our you? ', validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered? ")
    mood = RadioField("Please choose your mood: ",
                      choices=[('mood_one', 'Happy'), ('mood_two', 'Excited'), ('mood_three', 'Sleepy')])
    food_choice = SelectField(u"Pick your favorite food: ",
                              choices=[('chi', 'Chicken'), ('bf', 'Beef'), ('pk', 'Pork'), ('fish', 'Fish') ])
    feedback = TextAreaField("Please provide any feedback: ")
    submit = SubmitField("Submit Info")

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food_choice'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))
    
    return render_template('index.html', form=form, title=title)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html', title=title)

if __name__ == "__main__":
    app.run(debug=True)