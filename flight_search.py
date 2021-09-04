# Import necessary libraries
import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Volumes/Workstation/Learning Center/Data Science/"
                        "100 Days of Code - Complete Python Pro Bootcamp 2021/Projects/@CREDENTIALS/.env")

# Constants
KIWI_API_KEY = os.getenv("KIWI_API_KEY")


class FlightSearch:
    """A class to represent all the functionalities
    related to flight search"""
    def __init__(self, city: str):
        self.ENDPOINT = "https://tequila-api.kiwi.com"
        self.HEADER = {
            "apikey": KIWI_API_KEY,
        }
        self.city = city

    def kiwi_get_location(self):
        """Function to extract data from location API endpoint"""
        params = {
            "term": self.city,
            "location_types": "city",
        }
        response = requests.get(url=f"{self.ENDPOINT}/locations/query", headers=self.HEADER,
                                params=params)
        response.raise_for_status()
        data = response.json()
        return data
