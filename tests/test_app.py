from app import app
import pytest
import json

class TestApp:
    app.testing = True
    client = app.test_client()

    def test_healthcheck(self):
        response = app.test_client().get('/')
        assert response.status_code == 200

    def test_misinformation_handling(self):
        test_str = "This is a test"
        headers = {'header': 'header-info'}
        response = app.test_client().options('/misinformation', json={"text": test_str}, headers=headers)
        assert response.status_code == 204


    def test_misinformation_error_handling(self):
        with pytest.raises(Exception, match="Request text is empty"):
            test_str = ""
            response = app.test_client().post('/misinformation', json={"text": test_str})
