import requests

api_key = "05e6cb7e5a53d6939d94a2c634194c12"
api_call = "https://api.openweathermap.org/data/2.5/onecall"
MY_LAT = 37.322998
MY_LONG = -122.032181

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
}

response = requests.get(api_call, params=params)
response.raise_for_status()
data = response.json()
print(data)
