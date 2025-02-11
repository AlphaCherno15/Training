from flask import Flask, render_template
import random, datetime, post
app = Flask(__name__)


@app.route('/')
def home():
    lucky_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template('index.html', num=lucky_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    response1 = requests.get('https://api.genderize.io', params={'name': name})
    data1 = response1.json()
    response2 = requests.get('https://api.agify.io', params={'name': name})
    data2 = response2.json()

    return render_template('guess.html', name=name,age=data2["age"], gender=data1["gender"])

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    data = response.json()

    return render_template('blog.html', posts=data, num=num)


if __name__ == "__main__":
    app.run(debug=True)


