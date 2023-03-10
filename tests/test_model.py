from app import app
import pytest

class TestModel:
    app.testing = True
    client = app.test_client()

    head_str = "Content-Type: application/json; charset=utf-8\r\nAccess-Control-Allow-Origin: " +\
        "*\r\nAccess-Control-Allow-Methods: " + "*\r\nAccess-Control-Allow-Headers: *\r\n\r\n"

    def test_option_headers(self):
        response = app.test_client().options('/misinformation', json={"text": ""})
        assert response.status_code == 204
        assert str(response.headers) == self.head_str

    def test_model_simple_false(self):
        test_str = "Obama was the first U.S. president."
        response = app.test_client().post('/misinformation',
                                          json={"text": test_str, "user": "test_user1"})
        assert response.status_code == 200
        assert response.text == "{\"valid\": false}"

    def test_model_simple_true(self):
        test_str = "Earth has one moon."
        response = app.test_client().post('/misinformation',
                                          json={"text": test_str, "user": "test_user2"})
        assert response.status_code == 200
        assert response.text == "{\"valid\": true}"

    def test_model_complex(self):
        test_str = "Donald Trump won the 2020 election."
        response = app.test_client().post('/misinformation',
                                          json={"text": test_str, "user": "test_user3"})
        assert response.status_code == 200
        assert response.text == "{\"valid\": false}"