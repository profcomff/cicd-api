import pytest
from fastapi.testclient import TestClient
from app.routes.base import app


@pytest.fixture
def client(mocker):
    mocker.patch("auth_lib.fastapi.UnionAuth.__call__", return_value={"email": "test"})
    client = TestClient(app)
    return client
