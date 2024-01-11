#This file will need to use the DataManager,FlightSearch,
# FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

dm = DataManager()
dm.get_data()
fs = FlightSearch()

for dest in dm.sheet_data:
    if dest["iataCode"] == "":
        dest["iataCode"] = fs.get_code(dest["city"])
        dm.updated_row_id.append(dest["id"])

for dest in dm.sheet_data:
    flight = fs.get_data(dest["iataCode"])
    if flight is not None and flight.price < dest["lowestPrice"]:
        dest["lowestPrice"] = flight.price

dm.update_data()
