# Import necessary libraries
import os
import requests
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv

load_dotenv(dotenv_path="/Volumes/Workstation/Learning Center/Data Science/"
                        "100 Days of Code - Complete Python Pro Bootcamp 2021/Projects/@CREDENTIALS/.env")

# Constants
KIWI_API_KEY = os.getenv("KIWI_API_KEY")

# Constants
FLY_FROM = "DAC"

# Variables for time duration of flight search
date_from = datetime.today().date() + timedelta(days=1)
date_to = date_from + relativedelta(months=6)


class FlightData:
    """A class to represent all the functionalities
    related to flight data"""
    def __init__(self):
        self.ENDPOINT = "https://tequila-api.kiwi.com"
        self.HEADER = {
            "apikey": KIWI_API_KEY,
        }

    def flight_search_get_request(self, iata_code: str):
        """Function for getting all the flight data
        for desired destination"""
        params = {
            "fly_from": FLY_FROM,
            "fly_to": iata_code,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD",
        }
        response = requests.get(url=f"{self.ENDPOINT}/v2/search", headers=self.HEADER, params=params)
        response.raise_for_status()
        data = response.json()
        return data["data"]
