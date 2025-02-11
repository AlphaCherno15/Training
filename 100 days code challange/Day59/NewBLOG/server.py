from flask import Flask, render_template
from post import Post

app = Flask(__name__)

posts = Post()
all_posts = posts.text()
@app.route('/')
def home():
    return render_template("index.html", content=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<num>')
def post(num):
    return render_template("post.html",  content=all_posts, id=int(num))

if __name__ == "__main__":
    app.run(debug=True)