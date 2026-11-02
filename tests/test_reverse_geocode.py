import importlib.util
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
import requests

_spec = importlib.util.spec_from_file_location(
    "streamlit_app", Path(__file__).parents[1] / "app" / "streamlit_app.py"
)
app = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(app)


@pytest.fixture(autouse=True)
def _clear_cache():
    app._reverse_geocode.clear()


def _response(payload):
    resp = MagicMock()
    resp.json.return_value = payload
    return resp


def test_builds_city_state_country():
    payload = {"address": {"city": "Atlanta", "state": "Georgia", "country": "United States"}}
    with patch.object(app.requests, "get", return_value=_response(payload)):
        assert app.get_location_name(33.77, -84.39) == "Atlanta, Georgia, United States"


def test_failure_returns_unknown_and_is_not_cached():
    payload = {"address": {"city": "Atlanta", "state": "Georgia", "country": "United States"}}
    with patch.object(app.requests, "get", side_effect=requests.Timeout):
        assert app.get_location_name(33.77, -84.39) == "Unknown Location"
    # A later successful call for the same point must hit the API again, not reuse the failure.
    with patch.object(app.requests, "get", return_value=_response(payload)) as get:
        assert app.get_location_name(33.77, -84.39) == "Atlanta, Georgia, United States"
    assert get.call_count == 1


def test_http_error_returns_unknown():
    resp = _response({})
    resp.raise_for_status.side_effect = requests.HTTPError("429")
    with patch.object(app.requests, "get", return_value=resp):
        assert app.get_location_name(1.0, 2.0) == "Unknown Location"
