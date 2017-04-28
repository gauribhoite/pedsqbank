
from functools import wraps

from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for, flash

from blueprints import db, questions_list
from blueprints.models import Question, Chapter, Answer

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


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
@home_blueprint.route('/', methods=['GET', 'POST'])
@login_required
def home():
    questions = db.session.query(Question).all()
    chapters = db.session.query(Chapter).all()
    answers = db.session.query(Answer).all()
    if request.method == 'GET':
        return render_template("index.html", questions=questions, chapters=chapters, answers=answers)
    questions_list.append(request.form["answer"])
    return render_template("index.html", questions=questions, chapters=chapters, answers=answers)


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template
