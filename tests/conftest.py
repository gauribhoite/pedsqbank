import pytest
from app import create_app


@pytest.yield_fixture(scope="session")
def test_app():
    """
    Setup test flask app
    :return: Flask app
    """
    param = {
        'DEBUG': True,
        'TESTING': True
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
    yield test_app.test_client()