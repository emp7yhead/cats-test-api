from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_create_cat():
    response = client.post(
        '/api/v1/cats/',
        json={
            'name': 'Barsik',
            'color': 'black',
            'tail_length': 10,
            'whiskers_length': 20,
        },
    )
    assert response.status_code == 200, response.text
