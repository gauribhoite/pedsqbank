#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
    url_for, Blueprint
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user

from blueprints.models import User
from blueprints.users.decorators import anonymous_required
from blueprints.users.form import LoginForm, RegisterForm
from extensions import db




################
#### config ####
################
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
                print(user)
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


@users_blueprint.route('/register/', methods=['GET', 'POST'])
@anonymous_required()
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        print("post")
        print(form.name, form.username, form.email, form.password)
        print(form.name, form.username, form.email, request.form['password'])

        if form.validate_on_submit():
            print("validate")
            user = User(
                username=form.username.data,
                email=form.email.data,
                password=form.password.data,
                name=form.name.data
            )
            # user = User()

            # form.populate_obj(user)
            print(user)

            user.registered=True
            db.session.add(user)
            db.session.commit()
            # login_user(user)
            print("user: ",user)
            if login_user(user):
                print("login")
                flash('Awesome, thanks for signing up!', 'success')
                return redirect(url_for('home.welcome'))
    return render_template('register.html', form=form)