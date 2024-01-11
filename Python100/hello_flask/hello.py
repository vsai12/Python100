from flask import Flask

app = Flask(__name__)


def make_bold(func):
    def wrapper_func():
        return '<b>' + func() + '</b>'

    return wrapper_func


def make_emphasis(func):
    def wrapper_func():
        return '<em>' + func() + '</em>'

    return wrapper_func


def make_underlined(func):
    def wrapper_func():
        return '<u>' + func() + '</u>'

    return wrapper_func


@app.route('/')
def hello_world():
    return "Hello, World!"


@app.route("/bye")
@make_bold
def bye():
    return "Bye!"


app.route("/username/<name>/<int:number>")


def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)
