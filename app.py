from functools import wraps

from flask import Flask, render_template
from flask import flash
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.BaseConfig')

db = SQLAlchemy(app)
from models import *


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash("You need to log in to continue")
            return redirect(url_for("login"))

    return wrapper


@app.route('/')
@login_required
def home():
    questions = db.session.query(Question).all()
    chapters = db.session.query(Chapter).all()
    answers = db.session.query(Answer).all()
    return render_template("index.html", questions=questions, chapters=chapters, answers=answers)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))

    return render_template('login.html', error=error)


@app.route("/logout")
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run()
