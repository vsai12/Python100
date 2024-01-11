# This class is responsible for talking to the Flight Search API.
from datetime import datetime, timedelta
from pprint import pprint

import requests

from flight_data import FlightData

FLIGHT_ENDPOINT = "https://api.tequila.kiwi.com/"
FLIGHT_API_KEY = "dB3RoRrrmRlrwB6oId8vPL1ebDxg9I6o"
FLIGHT_FLY_FROM = "LON"


class FlightSearch:
    def __init__(self):
        self.uses = 0

    def get_code(self, city):
        self.uses += 1
        header = {
            "apikey": FLIGHT_API_KEY,
        }

        query = {
            "term": city,
            "location_types": "city",
            "limit": 1,
        }

        flight_resp = requests.get(url=f"{FLIGHT_ENDPOINT}locations/query?", params=query, headers=header)
        flight_resp.raise_for_status()
        f_data_code = flight_resp.json()["locations"][0]["code"]
        return f_data_code

    def get_data(self, code):
        self.uses += 1
        now = datetime.now()
        tmr = now + timedelta(days=1)
        format_tmr = tmr.strftime("%d/%m/%Y")
        end_date = now + timedelta(days=180)
        format_end = end_date.strftime("%d/%m/%Y")

        header = {
            "apikey": FLIGHT_API_KEY,
        }

        query = {
            "fly_from": FLIGHT_FLY_FROM,
            "fly_to": code,
            "date_from": format_tmr,
            "date_to": format_end,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "max_stopovers": 0,
            "ret_from_diff_city": False,
            "ret_to_diff_city": False,
            "curr": "GBP",
            "limit": 1,
        }

        flight_resp = requests.get(url=f"{FLIGHT_ENDPOINT}search?", params=query, headers=header)
        flight_resp.raise_for_status()
        try:
            data = flight_resp.json()["data"][0]
        except IndexError:
            print(f"No flights found for {code}.")
            return None
        f_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=datetime.utcfromtimestamp(data["route"][0]["dTimeUTC"]).strftime("%Y-%m-%d"),
            return_date=datetime.utcfromtimestamp(data["route"][1]["dTimeUTC"]).strftime("%Y-%m-%d"),
        )
        print(f"{f_data.destination_city}: £{f_data.price}")
        return f_data



