import requests
from pprint import pprint
SHEET_ENDPOINT = "https://api.sheety.co/d680e9f722df535083a37d12973cb161/flightDeals/sheet1"


class DataManager:

    def __init__(self):
        self.destination_date = {}

    def get_destination_data(self):
        response = requests.get(url=SHEET_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data



    pass