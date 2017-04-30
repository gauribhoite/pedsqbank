import pytest

from app import create_app
from blueprints.models import User
from extensions import db as _db
from tests import config


@pytest.yield_fixture(scope="session")
def test_app():
    """
    Setup test flask app
    :return: Flask app
    """

    param = {
        'DEBUG': True,
        'TESTING': True,
        'WTF_CSRF_ENABLED': False,
        'SQLALCHEMY_DATABASE_URI': config.TestBaseConfig.SQLALCHEMY_DATABASE_URI
    }
    _app = create_app(settings_override=param)
    ctx = _app.app_context()
    ctx.push()
    yield _app
    ctx.pop()


@pytest.yield_fixture(scope='function')
def client(test_app):
    """
    Setup an app client
    :param test_app: Pytest fixture
    :return: Flask app client
    """
    print("yielded test_app client")
    yield test_app.test_client()


@pytest.fixture(scope='session')
def db(test_app):
    """
    Setup our database, this only gets executed once per session.

    :param app: Pytest fixture
    :return: SQLAlchemy database session
    """
    _db.drop_all()
    _db.create_all()
    print('db fixture')
    # Create a single user because a lot of tests do not mutate this user.
    params = {
        'username': 'admin',
        'email': 'admin@local.host',
        'password': 'password',
        'name': 'Test',
    }

    admin = User(**params)
    # admin.username = 'admin'
    # admin.email = 'admin@local.host'
    # admin.password = 'password'
    admin.name = 'Admin'
    admin.registered =True

    _db.session.add(admin)
    _db.session.commit()

    return _db

