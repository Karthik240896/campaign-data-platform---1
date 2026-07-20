import requests

class WindsorClient:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def get_data(self, connector: str, date_from: str, date_to: str):
        params = {"api_key": self.api_key, "date_from": date_from, "date_to": date_to}
        resp = requests.get(f"{self.base_url}/{connector}", params=params)
        resp.raise_for_status()
        return resp.json()["data"]
