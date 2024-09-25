from flask import Flask, render_template #Flask will look for templates subdir
from flask_bootstrap import Bootstrap

#application instance is an object of class Flask
app = Flask(__name__) #takes the name of the main module as the required argument, using Python's name var here
bootstrap = Bootstrap(app)
@app.route('/')
def index(): #index is the handler for the main root URL, view function
 return render_template('index.html')

@app.route('/user/<name>') #dynamic, second route, respond with the personalized greeting using the name dynamic argument
def user(name):
 return render_template('user.html', name=name)