import requests

SEARCH_ENDPOINT = "https://tequila-api.kiwi.com"
api_key = "*********"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{SEARCH_ENDPOINT}/locations/query"
        headers = {"apikey": api_key}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

