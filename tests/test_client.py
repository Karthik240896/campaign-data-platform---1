import responses
from windsor.client import WindsorClient

@responses.activate
def test_get_data_returns_rows():
    responses.add(
        responses.GET,
        "https://connectors.windsor.ai/google_ads",
        json={"data": [{"date": "2026-07-01", "campaign_name": "Test", "spend": 10.5}]},
        status=200,
    )
    client = WindsorClient(api_key="fake", base_url="https://connectors.windsor.ai")
    rows = client.get_data("google_ads", "2026-07-01", "2026-07-07")
    assert rows[0]["campaign_name"] == "Test"
