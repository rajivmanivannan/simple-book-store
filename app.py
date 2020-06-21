from os import environ, path
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from wtforms import Form, StringField, validators
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


app = Flask(__name__)

app.config.from_object(environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    author = db.Column(db.String())
    published = db.Column(db.String())

    def __init__(self, name, author, published):
        self.name = name
        self.author = author
        self.published = published

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'published': self.published
        }

class AddBookForm(Form):
    name = StringField('name', [validators.required(),validators.Length(min=1, max=100)])
    author = StringField('author', [validators.required(),validators.Length(min=1, max=100)])
    published = StringField('published', [validators.optional()])

@app.route("/")
def get_all():
    try:
        books = Book.query.all()
        return render_template("index.html", books=books)
    except Exception as e:
        return(str(e))
    return render_template("index.html")

@app.route("/add", methods=['GET', 'POST'])
def add_book_form():
    form = AddBookForm(request.form)
    if request.method == 'POST' and form.validate():
        try:
            book = Book(
                name=form.name.data,
                author=form.author.data,
                published=form.published.data
            )
            db.session.add(book)
            db.session.commit()
            message = "Book added to the store successfully. Book id is {}".format(
                book.id)
            return render_template("addbook.html", message=message)
        except Exception as e:
            return(str(e))
    return render_template("addbook.html",form=form)

if __name__ == '__main__':
    app.run()
