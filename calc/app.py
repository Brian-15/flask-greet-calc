# Put your app in here.
import operations

from flask import Flask, request

app = Flask(__name__)

@app.route("/add")
def add():
    """adds two parameters from query arguments and displays the result"""

    [a, b] = [int(request.args["a"]), int(request.args["b"])]

    return f"""{operations.add(a, b)}"""

@app.route("/sub")
def sub():
    """subtracts two parameters from query arguments and displays the result"""
    
    [a, b] = [int(request.args["a"]), int(request.args["b"])]

    return f"""{operations.sub(a, b)}"""


@app.route('/mult')
def mult():
    """multiplies two numbers and displays product"""

    [a, b] = [int(request.args["a"]), int(request.args["b"])]

    return f"""{operations.mult(a, b)}"""

@app.route("/div")
def div():
    """divides two numbers and displays result"""

    [a, b] = [int(request.args["a"]), int(request.args["b"])]

    return f"""{operations.div(a, b)}"""

@app.route("/math/<operation>")
def math(operation):

    if operation == "add":
        return add()
    elif operation == "sub":
        return sub()
    elif operation == "mult":
        return mult()
    elif operation == "div":
        return div()
    else:
        return "Operation Not Found"