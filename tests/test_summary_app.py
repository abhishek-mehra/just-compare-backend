import json
import pytest

from just_compare_backend.backend import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_generate_summary(client):
    # Define the input data for the test
    input_data = {
        "text1": "This is a sample text.",
        "text2": "This is another sample text.",
    }

    # Make a POST request to the endpoint with the input data
    response = client.post("/generate_summary", json=input_data)

    # Assert that the response has a 200 status code
    assert response.status_code == 200

    # Parse the JSON response
    data = json.loads(response.data.decode())

    # Assert that the summary is not empty
    assert data["summary"] != ""
