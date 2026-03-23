import logging

import httpx

logger = logging.getLogger(__name__)

BASE_URL = "http://localhost:8090"


def test_estimate_time_returns_200():
    response = httpx.get(f"{BASE_URL}/estimate-time/5.0")
    assert response.status_code == 200


def test_estimate_time_correct_value():
    response = httpx.get(f"{BASE_URL}/estimate-time/5.0")
    expected = 10 + 5 * 5.0
    assert response.json()["estimated_delivery_time_minutes"] == expected


def test_estimate_time_zero_distance():
    response = httpx.get(f"{BASE_URL}/estimate-time/0")
    assert response.json()["estimated_delivery_time_minutes"] == 10


def test_estimate_time_has_correct_key():
    response = httpx.get(f"{BASE_URL}/estimate-time/5.0")
    assert "estimated_delivery_time_minutes" in response.json()


def test_estimate_time_invalid_param():
    response = httpx.get(f"{BASE_URL}/estimate-time/abc")
    assert response.status_code == 422
