# This class is responsible for talking to the Google Sheet.
from pprint import pprint

import requests

SHEET_ENDPOINT = "https://api.sheety.co/7cd147b98422615df03c6422445f8864/flightDeal/prices"


class DataManager:
    def __init__(self):
        self.sheet_data = []
        self.updated_row_id = []

    def get_data(self):
        sheet_resp = requests.get(url=SHEET_ENDPOINT)
        sheet_resp.raise_for_status()
        self.sheet_data = sheet_resp.json()["prices"]

    def update_data(self):
        for row in self.updated_row_id:
            params = {
                "price": self.sheet_data[row - 2]
            }
            sheet_resp = requests.put(url=f"{SHEET_ENDPOINT}/{row}", json=params)
            sheet_resp.raise_for_status()
        self.updated_row_id.clear()
