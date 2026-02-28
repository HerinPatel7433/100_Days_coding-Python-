import requests
from datetime import datetime

USERNAME = "herin"
TOKEN = "za344fekvklfdfa"
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you code today? "),
}

response = requests.post(url=PIXEL_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)
