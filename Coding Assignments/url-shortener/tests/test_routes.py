import pytest
from fastapi.testclient import TestClient

from src.main import app
from src.utils.store_connector import StoreConnector

client = TestClient(app)


def test_shorten():
    """
    Test "shorten" route. It should return 200 response with valid response body.
    """
    response = client.post("/shorten", json={"url": "https://www.google.com"})
    assert response.status_code == 200
    assert response.json() == {"url": "http://testserver:None/ac6bb669"}

    store = StoreConnector().store
    assert "ac6bb669" in store and store["ac6bb669"] == "https://www.google.com"


def test_shorten_multiple_times():
    """
    When called multiple times with the same long URL, response should be same
    without adding new entries in the store.
    """
    response = client.post("/shorten", json={"url": "https://www.google.com"})
    assert response.status_code == 200
    assert response.json() == {"url": "http://testserver:None/ac6bb669"}

    response = client.post("/shorten", json={"url": "https://www.google.com"})
    assert response.status_code == 200
    assert response.json() == {"url": "http://testserver:None/ac6bb669"}

    store = StoreConnector().store
    assert "ac6bb669" in store and store["ac6bb669"] == "https://www.google.com"


def test_redirect():
    """
    When called with shortened URL, test the redirection.
    """
    store = StoreConnector().store
    store["ac6bb669"] = "https://www.google.com"
    assert client.get("/ac6bb668").status_code == 404


@pytest.mark.parametrize(
    "endpoint_url, expected",
    [
        ("http://localhost:27015/shorten", "http://localhost:27015"),
        ("https://3.14.102.57:80/shorten", "https://3.14.102.57:80"),
        ("https://dummy-domain:8080/shorten", "https://dummy-domain:8080"),
        ("http://dummy-domain:8080/shorten", "http://dummy-domain:8080"),
    ],
)
def test_get_base_url(endpoint_url, expected):
    """
    Test base URL extraction.
    """
    from src.routes.urls import _get_base_url

    assert _get_base_url(endpoint_url) == expected
