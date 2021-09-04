# Import necessary libraries
import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Volumes/Workstation/Learning Center/Data Science/"
                        "100 Days of Code - Complete Python Pro Bootcamp 2021/Projects/@CREDENTIALS/.env")
SHEETY_API_KEY = os.getenv("SHEETY_API_FLIGHT")


class DataManager:
    """A class to represent all the functionalities
    of the Sheety API."""
    def __init__(self):
        self.ENDPOINT = f"https://api.sheety.co/{SHEETY_API_KEY}/flightDeals/prices"

    def sheety_get_response(self):
        """Function to get the response from google sheet"""
        response = requests.get(url=self.ENDPOINT)
        response.raise_for_status()
        data = response.json()
        return data

    def sheety_put_request(self, iata_code: str, row_id: int):
        """Function to update iata code"""
        params = {
            "price": {
                "iataCode": iata_code,
            }
        }
        response = requests.put(url=f"{self.ENDPOINT}/{row_id}", json=params)
        print(response.text)
