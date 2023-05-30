from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client


# Test root
def test_get_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Main Server Hello World"}
