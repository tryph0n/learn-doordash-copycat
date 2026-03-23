import logging

import httpx

logger = logging.getLogger(__name__)

BASE_URL = "http://localhost:8090"


def test_status_returns_200():
    response = httpx.get(f"{BASE_URL}/status/")
    assert response.status_code == 200


def test_status_returns_correct_json():
    response = httpx.get(f"{BASE_URL}/status/")
    assert response.json() == {"status": "Service is up and running"}
