from datetime import datetime
# Flask will look for templates subdir
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email


# application instance is an object of class Flask
# takes the name of the main module as the required argument, using Python's name var here
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# dynamic, second route, respond with the personalized greeting using the name dynamic argument
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


#def checkUToronto(form,field):
 #   if ("utoronto.ca" not in field.data):
  #      raise ValidationError("Must be a utoronto.ca email")


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT Email Address?', validators=[DataRequired(),Email()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        #return redirect(url_for('index'))

        old_email = session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['email'] = form.email.data
        return redirect(url_for('index'))

    return render_template('index.html',
                           form=form, name=session.get('name'), email=session.get('email'))
