import requests as rq, os
from dotenv import load_dotenv
load_dotenv()

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self._post_endpoint = os.environ["sheety_endpoint"]
        self._bearer_headers = {
            "Authorization": f"Bearer {os.environ["sheety_api_secret"]}"
        }
    def post(self):
        inputs = {
            "flight":{
                "city": "New York",
                "iataCode": "JFK",
                "lowestPrice": "200",
            }
        }
        write = rq.post(self._post_endpoint, json=inputs, headers=self._bearer_headers)
        print(write.text)
    def read(self):
        read_file = rq.get(self._post_endpoint, headers=self._bearer_headers)
        dt = read_file.json()
        return dt["flights"]
    def edit(self, iata, price, row):
        inputs = {
            "flight": {
                "iataCode": iata,
                "lowestPrice": price
            }
        }
        rq.put(f'{self._post_endpoint}/{row}', json=inputs, headers=self._bearer_headers)