import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_task(client):
    response = client.post('/tasks', json={'task': 'Write unit tests'})
    assert response.status_code == 201
    assert response.get_json()['message'] == 'Task added!'

def test_get_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
