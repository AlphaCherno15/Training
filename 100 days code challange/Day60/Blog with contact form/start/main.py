from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    name = request.form['name']
    password = request.form['password']
    return f'<h1>Name: {name}</h1><h1>Password: {password}</h1>'

if __name__ == "__main__":
    app.run(debug=True)