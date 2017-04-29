from flask import Blueprint
from flask import render_template
from flask import request
from flask_login import login_required

from blueprints.models import Question, Chapter, Answer
from extensions import db

home_blueprint = Blueprint(
    'home', __name__,
    template_folder='templates'
)


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
    # questions_list.append(request.form["answer"])
    return render_template("index.html", questions=questions, chapters=chapters, answers=answers)


@home_blueprint.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template
