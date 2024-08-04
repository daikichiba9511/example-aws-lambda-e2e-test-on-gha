import os
import json
import requests
import pytest


ORIGIN = os.getenv("ORIGIN", "http://localhost:8080")


@pytest.fixture
def sample_success_request() -> str:
    return json.dumps({"message": "Hello, World!"})


def test_app_should_success(sample_success_request: str) -> None:
    response = requests.get(
        f"{ORIGIN}/2015-03-31/functions/function/invocations",
        data=sample_success_request,
    )

    assert getattr(response, "status_code") == 200, (
        f"Requested to {ORIGIN}. Expected status code 200, but got {response.status_code} "
        + "You should check the environment variable ORIGIN in compose.yaml. "
        + "If you are on GitHub Action, please check 'http://server:8080' is allowed. "
    )

    response_json = response.json()
    assert response_json.get("message") == "Hello, World!", (
        f"Requested to {ORIGIN}. Expected message 'Hello, World!', but got {response_json.get('message')} "
        + f"RESPONSE_JSON: {response_json}"
    )
