import logging

import httpx

logger = logging.getLogger(__name__)

BASE_URL = "http://localhost:8090"


def test_root_returns_200():
    response = httpx.get(f"{BASE_URL}/")
    assert response.status_code == 200


def test_root_returns_welcome_message():
    response = httpx.get(f"{BASE_URL}/")
    assert response.json() == {"message": "Welcome to the DoorDash Delivery Fee Service API"}
