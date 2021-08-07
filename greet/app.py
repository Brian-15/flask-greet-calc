from flask import Flask, request

app = Flask(__name__)

@app.route('/welcome')
def welcome():
    """Welcome Page"""

    return "<h1>welcome</h1>"

@app.route('/welcome/home')
def welcome_home():
    """Welcome Home Page"""

    return "<h1>welcome home</h1>"

@app.route('/welcome/back')
def welcome_back():
    """Welcome Back Page"""

    return "<h1>welcome back</h1>"