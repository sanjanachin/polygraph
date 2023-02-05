from app import app
import pytest

class TestApp:
    app.testing = True
    client = app.test_client()

    def test_healthcheck(self):
        response = app.test_client().get('/')
        assert response.status_code == 200