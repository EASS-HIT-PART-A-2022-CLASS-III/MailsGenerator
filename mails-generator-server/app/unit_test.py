from fastapi.testclient import TestClient
import pytest

from main import app
from mailsGenerator import *

client = TestClient(app)


@pytest.fixture(scope="module")
def test_client():
    with TestClient(app) as client:
        yield client


# Test root
def test_get_root(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@pytest.mark.asyncio
async def test_generateMailFromChatgpt():
    test_prompt = "hello world"
    response = await tryGeneratingMailFromChatgpt(test_prompt)
    assert response != ""
