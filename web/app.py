from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.getenv('MYSQL_USERNAME')}:{os.getenv('MYSQL_PASSWORD')}@db/{os.getenv('MYSQL_DATABASE')}"
db = SQLAlchemy(app)


class Person(db.Model):

    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer(), nullable=True)

    def __str__(self):
        return f"<Person Id={self.id}, Name={' '.join([self.FirstName, self.LastName])}>"


@app.route('/')
def hello_world():

    people = Person.query.all()

    return render_template("people.html", people=people)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
