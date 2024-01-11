from datetime import datetime

import requests

USERNAME = "vsai12"
TOKEN = "imfn230f2f02inf20n"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Create an user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_create_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime(year=2023, month=10, day=24)
today = today.strftime("%Y%m%d")

pixel_params = {
    "date": today,
    "quantity": "4",
}

# Add a pixel
# response = requests.post(url=pixel_create_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_create_endpoint}/{today}"

update_params = {
    "quantity": "2"
}

# Update a pixel
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(response.text)

response = requests.delete(url=update_endpoint, headers=headers)
print(response.text)
