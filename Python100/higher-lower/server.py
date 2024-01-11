from flask import Flask
import random

app = Flask(__name__)

HOME_GIF = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
LOW_GIF = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
HIGH_GIF = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
CORRECT_GIF = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"


@app.route("/")
def home_page():
    return (f'<h1>Guess a number between 0 and 9</h1>'
            f'<img src={HOME_GIF}>')


winner = random.randint(0, 9)


@app.route("/<int:num>")
def check_ans(num):
    if num < winner:
        return (f'<h1 style="color:red;">Too low, try again!</h1>'
                f'<img src={LOW_GIF}>')
    elif num == winner:
        return (f'<h1 style="color:green;">You found me!</h1>'
                f'<img src={CORRECT_GIF}>')
    else:
        return (f'<h1 style="color:purple;">Too high, try again!</h1>'
                f'<img src={HIGH_GIF}>')


if __name__ == '__main__':
    app.run(debug=True)
