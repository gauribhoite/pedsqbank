#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
    url_for, Blueprint


################
#### config ####
################
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from blueprints.models import User
from blueprints.users.form import LoginForm

users_blueprint = Blueprint(
    'users', __name__,
    template_folder='templates'
)


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
                # session['logged_in'] = True
                login_user(user)
                flash('You were logged in.')
                return redirect(url_for('home.home'))
            else:
                error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', form=form, error=error)


@users_blueprint.route('/logout')
@login_required
def logout():
    # session.pop('logged_in', None)
    logout_user()
    flash('You were logged out.')
    return redirect(url_for('home.welcome'))
