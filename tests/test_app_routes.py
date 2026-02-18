import pytest
from src.app import create_app
import json

def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "Brent Oil API is running"
def test_prices_route(client):
    response = client.get("/prices")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert "Date" in data[0]
def test_events_route(client):
    response = client.get("/events")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert "Date" in data[0]
def test_change_points_route(client):
    response = client.get("/change_points")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert "T" in data[0], "Change points should be in ISO format"
