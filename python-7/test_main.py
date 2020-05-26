import requests

from main import get_temperature


class MockResponse:

    def __init__(self, mock_temperature):
        self.mock_temperature = mock_temperature

    def json(self):
        return {
            "currently": {
                "temperature": self.mock_temperature
            }}


def mock_get_temperature(url, temperature):
    return MockResponse(temperature)


def test_get_temperature_by_lat_lng(monkeypatch):

    def mock_get_temperature(url):
        return MockResponse(62)

    lat = -14.235004
    lng = -51.92528

    monkeypatch.setattr(requests, 'get', mock_get_temperature)
    response = get_temperature(lat, lng)

    assert response == 16


def test_temperature_returns_none(monkeypatch):

    def mock_get_temperature(url):
        return MockResponse(None)

    lat = 0.0
    lng = 0.0

    monkeypatch.setattr(requests, 'get', mock_get_temperature)
    response = get_temperature(lat, lng)

    assert response is None
