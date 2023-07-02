# Put your app in here.
from flask import Flask,request
from flask_debugtoolbar import DebugToolbarExtension
from operations import add,sub,div,mult

app = Flask(__name__)


@app.route("/")
def show_home():
    return "Welcome home"
# VARS = {
#     a:request.args["a"]
# }

@app.route("/add")
def show_addition():
    a =  int(request.args["a"])
    b =  int(request.args["b"])

    add_func = add(a,b)
    return str(add_func)


@app.route("/sub")
def show_subtration():
    a =  int(request.args["a"])
    b =  int(request.args["b"])

    sub_func = sub(a,b)
    return str(sub_func)


@app.route("/div")
def show_division():
    a =  int(request.args["a"])
    b =  int(request.args["b"])

    div_func = div(a,b)
    return str(int(div_func))

@app.route("/multi")
def show_multiplication():
    a =  int(request.args["a"])
    b =  int(request.args["b"])

    multi_func = mult(a,b)
    return str(multi_func)
oper =  {
    "add":add,
    "sub":sub,
    "div":div,
    "multi":mult,

}

@app.route("/math/<operation>")
def math_ops(operation):
    a =  int(request.args["a"])
    b =  int(request.args["b"])
    math_operation = oper[operation](a,b)
    return str(math_operation)

