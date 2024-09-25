from datetime import datetime
from flask import Flask, render_template #Flask will look for templates subdir
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


#application instance is an object of class Flask
app = Flask(__name__) #takes the name of the main module as the required argument, using Python's name var here
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.errorhandler(404)
def page_not_found(e):
 return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
 return render_template('500.html'), 500

@app.route('/') #index is the handler for the main root URL, view function
def index():
 return render_template('index.html',
 current_time=datetime.utcnow())

@app.route('/user/<name>') #dynamic, second route, respond with the personalized greeting using the name dynamic argument
def user(name):
 return render_template('user.html', name=name)

 class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')
