import pytest
from flask import url_for
from blueprints.models import User


class TestLogin(object):
    def test_login_page(self, client, db):
        response = client.get(url_for('users.login'))
        assert response.status_code == 200

    def test_login(self, client, db, username='admin', password='password'):
        """ Login successfully. """
        user = dict(username=username, password=password)
        response = client.post(url_for('users.login'), data=user,
                               follow_redirects=True)
        assert "Welcome to PedsQbank" in str(response.data)

    def test_logout(self, client, db, username='admin', password='password'):
        """ Logout successfully. """
        user = dict(username=username, password=password)
        client.post(url_for('users.login'), data=user, follow_redirects=True)
        response = client.get(url_for('users.logout'), follow_redirects=True)
        assert "You were logged out." in str(response.data)
        assert response.status_code == 200

    def test_main_route_requires_login(self, db, client):
        response = client.get('/', follow_redirects=True)
        assert 'Please log in to access this page' in str(response.data)

    def test_register_page(self, db, client):
        response = client.get(url_for('users.register'))
        assert response.status_code == 200

    @pytest.mark.parametrize("username, password", [
        ("incorrect","incorrect"),
        ("admin","incorrect"),
        ("incorrect","password")
    ])
    def test_invalid_login(self, client, db, username, password):
        invalid_user = dict(username=username, password=password)
        response = client.post(url_for('users.login'), data=invalid_user, follow_redirects=True)
        assert "Invalid Credentials. Please try again." in str(response.data)


class TestRegister(object):
    def test_valid_registration(self, client, db):
        old_user_count = User.query.count()
        client.post('/register/', data=self.register_user_data())
        new_user_count = User.query.count()
        assert (old_user_count + 1) == new_user_count
        new_user = User.query.filter(
            (User.email == self.register_user_data()['email']) | (
            User.username == self.register_user_data()['username'])).first()
        assert new_user.password == 'password1'

    def test_check_validation_on_email(self, client):
        response = client.post('/register/', data=self.register_user_data(username=''))
        assert "This field is required." in str(response.data)

    def test_check_validation_on_password(self, client):
        response = client.post('/register/', data=self.register_user_data(password=''))
        assert "This field is required." in str(response.data)

    def test_check_validation_on_password_match(self, client):
        response = client.post('/register/', data=self.register_user_data(confirm='mismatch'))
        assert "Passwords must match." in str(response.data)

    def register_user_data(self, name='Testing User', username='PyTest', password='password1',
                           email='testuser@emaple.com', confirm='password1'):
        return {
            'name': name,
            'username': username,
            'password': password,
            'email': email,
            'confirm': confirm
        }
