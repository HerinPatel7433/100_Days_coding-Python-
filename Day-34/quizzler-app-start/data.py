import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

respones = requests.get("https://opentdb.com/api.php", params=parameters)
respones.raise_for_status()
data = respones.json()
question_data = data["results"]

