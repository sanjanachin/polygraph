from app import app
import pytest

class TestApp:
    app.testing = True
    client = app.test_client()

    def test_healthcheck(self):
        response = app.test_client().get('/')
        assert response.status_code == 200

    def test_misinformation(self):
        test_str = "This is a test"
        response = app.test_client().post('/misinformation', json={"text": test_str})
        assert response.status_code == 200
        assert response.text == test_str