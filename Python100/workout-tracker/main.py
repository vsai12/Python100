from datetime import datetime
import pprint

import requests

APP_ID = "e50be39f"
API_KEY = "c8512011e9b5ed8bbc0dda1ab181d5a4"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT = 68.1
HEIGHT = 181
AGE = 23

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    # "Content-Type": "application/json",
}

user_input = input("Tell mew which exercises you did: ")

params = {
    "query": user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(url=EXERCISE_ENDPOINT, json=params, headers=headers)
response.raise_for_status()
data = response.json()["exercises"]

SHEET_ENDPOINT = "https://api.sheety.co/7cd147b98422615df03c6422445f8864/workoutTracking/workouts"
SHEET_USERNAME = "vsai12"
SHEET_PASSWORD = "3iq9cu3t48039ci3me"
sheet_header = {
    "Authorization": "Basic dnNhaTEyOjNpcTljdTN0NDgwMzljaTNtZQ==",
    "Content-Type": "application/json",
}

now = datetime.now()
format_date = now.strftime("%d/%m/%Y")
format_time = now.strftime("%H:%M:%S")

for e in data:
    body = {
        "workout": {
            "date": format_date,
            "time": format_time,
            "exercise": e["name"].title(),
            "duration": e["duration_min"],
            "calories": e["nf_calories"],
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=body, headers=sheet_header)
    sheet_response.raise_for_status()
    print(sheet_response.text)



