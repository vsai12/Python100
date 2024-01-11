from flask import Flask, render_template
import random
import datetime
import requests

GENDERIZE_URL = "https://api.genderize.io?"
AGIFY_URL = "https://api.agify.io/?"
app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    return render_template("index.html",
                           num=random_number,
                           CURRENT_YEAR=year,
                           YOUR_NAME="Vincent Huang")


@app.route('/guess/<name>')
def guess_name(name):
    name = name.title()
    params = {"name": name}
    g_resp = requests.get(GENDERIZE_URL, params)
    g_resp.raise_for_status()
    a_resp = requests.get(AGIFY_URL, params)
    a_resp.raise_for_status()
    gender = g_resp.json()["gender"]
    age = a_resp.json()["age"]
    return render_template("guess-name.html", gender=gender, age=age, name=name)


@app.route('/blog/<num>')
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    resp = requests.get(blog_url)
    all_posts = resp.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run()
