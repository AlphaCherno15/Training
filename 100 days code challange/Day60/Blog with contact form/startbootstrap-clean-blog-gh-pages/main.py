from flask import Flask, render_template, request
import requests, smtplib, os

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')
SMTP_ADRESS = os.environ.get('SMTP_ADRESS')
port = 587
app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    
    return render_template("contact.html",  send='no')


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    data = request.form
    name = data["name"]
    email = data["email"]
    phone = data["phone"]
    message = data["message"]
    text = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    print('Sending email...')
    with smtplib.SMTP(SMTP_ADRESS, port) as connection:
         # connection.ehlo()
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="alphacherno15@gmail.com",
            msg=f"Subject:User Message!\n\n{text}")

    return render_template("contact.html", send='yes')

if __name__ == "__main__":
    app.run(debug=True, port=5001)
