from flask import Flask


from extensions import db, login_manager


def create_app(settings_override=None):
    """
    Create a Flask application using the app factory pattern.

    :param settings_override: Override settings
    :return: Flask app
    """
    app = Flask(__name__)
    app.config.from_object('config.BaseConfig')

    if settings_override:
        app.config.update(settings_override)

    from blueprints.users.view import users_blueprint
    from blueprints.home.view import home_blueprint

    app.register_blueprint(users_blueprint)
    app.register_blueprint(home_blueprint)
    extensions(app)

    from blueprints.models import User
    login_manager.login_view = "users.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()
    return app


def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """
    db.init_app(app)
    login_manager.init_app(app)
    return None





####################
#### run server ####
####################
if __name__ == '__main__':
    app = create_app()
    app.run()
