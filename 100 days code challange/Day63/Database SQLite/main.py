from flask import Flask, render_template, request, redirect, url_for
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

all_books = []
class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250),unique=True , nullable=False)
    author: Mapped[str]= mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
    
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books-collection.db"
db.init_app(app)
@app.route('/')
def home():
    with app.app_context():
        all_books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=float(request.form["rating"])
        )
        with app.app_context():
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")

@app.route("/delete/<int:book_id>")
def delete(book_id):
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        if book_to_delete:
            db.session.delete(book_to_delete)
            db.session.commit()
    return redirect(url_for("home"))

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    with app.app_context():
        book_to_edit = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        if request.method == "POST":
            if book_to_edit:
                book_to_edit.rating = float(request.form["rating"])
                db.session.commit()
            return redirect(url_for("home"))
        return render_template("edit.html", book=book_to_edit)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

