from fastapi.testclient import TestClient

from app.main import app
import pytest

@pytest.fixture
def client():
    return TestClient(app=app)