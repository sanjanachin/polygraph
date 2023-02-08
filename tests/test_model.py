""" from app import app
import pytest

class TestModel:
    app.testing = True
    client = app.test_client()

    def test_model_simple_false(self):
        test_str = "Obama was the first U.S. president"
        response = app.test_client().post('/model', json={"text": test_str})
        print(response)
        assert response == "false"

    def test_model_simple_true(self):
        test_str = "Earth has one moon"
        response = app.test_client().post('/model', json={"text": test_str})
        print(response)
        assert response == "true"

    def test_model_complex(self):
        test_str = "Donald Trump won the 2020 election"
        response = app.test_client().post('/model', json={"text": test_str})
        print(response)
        assert response == "false" """