# save this as app.py
from flask import Flask

app = Flask(__name__)
print(__name__)
@app.route("/")
def hello():
    return "Hello, World!"