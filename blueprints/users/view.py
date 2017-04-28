#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint
from functools import wraps
from blueprints import db

################
#### config ####
################
from blueprints.models import User
from blueprints.users.form import LoginForm

users_blueprint = Blueprint(
    'users', __name__,
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

# route for handling the login page logic
@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    error = None
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=request.form['username']).first()
            if user is not None and request.form['password'] == user.password:
                session['logged_in'] = True
                flash('You were logged in.')
                return redirect(url_for('home.home'))
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('home.welcome'))
