import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app
import pytest
from unittest.mock import patch

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    with patch('app.cache.incr', return_value=1):
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello World! I have been seen' in response.data



