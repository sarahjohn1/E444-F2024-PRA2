from flask import Flask 

#application instance is an object of class Flask
app = Flask(__name__) #takes the name of the main module as the required argument, using Python's name var here
@app.route('/')
def index(): #index is the handler for the main root URL, view function
 return '<h1>Hello World!</h1>'

@app.route('/user/<name>') #dynamic, second route
def user(name):
 return '<h1>Hello, {}!</h1>'.format(name)