import pytest
from DataIncubatorApp import app
import io


@pytest.fixture
def client():
    test_client = app.test_client()
    return test_client


def test_index(client):
    response = client.get('/')
    html_text = 'Upload an image'
    assert html_text in str(response.data)


def test_upload(client):
    data = dict()
    image_name = b'test'
    data['picture'] = (io.BytesIO(image_name), '/static/test.png')
    response = client.post('/upload', content_type='multipart/form-data', data=data)
    assert response.data == image_name
