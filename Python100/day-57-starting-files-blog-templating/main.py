from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)
BLOG_API = "https://api.npoint.io/c790b4d5cab58020d391"
all_posts = []


@app.route('/blog')
def home():
    if len(all_posts) == 0:
        resp = requests.get(BLOG_API)
        data = resp.json()
        for post in data:
            all_posts.append(Post(post))

    return render_template("index.html", all_posts=all_posts)


@app.route('/post/<int:num>')
def blog(num):
    return render_template("post.html", post=all_posts[num - 1])


if __name__ == "__main__":
    app.run(debug=True)
