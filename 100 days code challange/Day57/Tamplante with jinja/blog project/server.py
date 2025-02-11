from flask import Flask, render_template
import  datetime, post
app = Flask(__name__)

posts = post.Post()
post1 = posts.text()
@app.route('/')
def home():

    current_year = datetime.datetime.now().year
    return render_template('index.html',  year=current_year,
                           title1=post1[0]["title"], content1=post1[0]["subtitle"],
                           title2=post1[1]["title"], content2=post1[1]["subtitle"]
                           )


@app.route('/post/<num>')
def get_post(num):
    data = posts.text()
    return render_template('post.html', content=data[int(num)]["body"], title=data[int(num)]["title"], subtitle=data[int(num)]["subtitle"])


if __name__ == "__main__":
    app.run(debug=True)
