from functools import wraps

from flask import Flask, render_template
from flask import abort
from flask import flash
from flask import redirect
from flask import request
from flask import session
from flask import url_for
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_object('config.BaseConfig')

db = SQLAlchemy(app)
questions_list = []
from models import *
from blueprints.users.view import users_blueprint
# register our blueprints
app.register_blueprint(users_blueprint)

##########################
#### helper functions ####
##########################


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


################
#### routes ####
################

# use decorators to link the function to a url
@app.route('/', methods=['GET', 'POST'])
@login_required
def home():

    questions = db.session.query(Question).all()
    chapters = db.session.query(Chapter).all()
    answers = db.session.query(Answer).all()
    if request.method == 'GET':
        return render_template("index.html", questions=questions, chapters=chapters, answers=answers)
    questions_list.append(request.form["answer"])
    return render_template("index.html", questions=questions, chapters=chapters, answers=answers)


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template


####################
#### run server ####
####################

if __name__ == '__main__':
    app.run()








