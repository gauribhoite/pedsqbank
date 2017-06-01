from flask_mail import Mail
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
# from flask_debugtoolbar import DebugToolbarExtension

db = SQLAlchemy()
login_manager = LoginManager()
# debug_toolbar = DebugToolbarExtension()
mail = Mail()
csrf = CSRFProtect()