from flask import url_for


class TestHome(object):
    def test_login_page(self, client):
        response = client.get(url_for('users.login'))
        assert response.status_code == 200
