import logging

import httpx

logger = logging.getLogger(__name__)

BASE_URL = "http://localhost:8090"


def test_fee_calculation_returns_200():
    response = httpx.post(f"{BASE_URL}/calculate-fee/", json={"distance_km": 5.0, "weight_kg": 2.0})
    assert response.status_code == 200


def test_fee_calculation_correct_value():
    response = httpx.post(f"{BASE_URL}/calculate-fee/", json={"distance_km": 5.0, "weight_kg": 2.0})
    expected = 5.0 + 1.5 * 5.0 + 0.5 * 2.0
    assert response.json()["delivery_fee"] == expected


def test_fee_calculation_zero_values():
    response = httpx.post(f"{BASE_URL}/calculate-fee/", json={"distance_km": 0, "weight_kg": 0})
    assert response.json()["delivery_fee"] == 5.0


def test_fee_calculation_has_delivery_fee_key():
    response = httpx.post(f"{BASE_URL}/calculate-fee/", json={"distance_km": 1.0, "weight_kg": 1.0})
    assert "delivery_fee" in response.json()


def test_fee_calculation_missing_field():
    response = httpx.post(f"{BASE_URL}/calculate-fee/", json={"distance_km": 5.0})
    assert response.status_code == 422


def test_fee_calculation_invalid_type():
    response = httpx.post(f"{BASE_URL}/calculate-fee/", json={"distance_km": "abc", "weight_kg": 2.0})
    assert response.status_code == 422
