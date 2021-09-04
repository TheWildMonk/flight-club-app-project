# Import necessary libraries
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Constants
DEPARTURE_CITY = "DHAKA"
DEPARTURE_CITY_IATA_CODE = "DAC"

# Sheety object definition
sheet_data_manager = DataManager()
sheet_data = sheet_data_manager.sheety_get_response()

# Flight data object definition
flight_data_manager = FlightData()

# Notification Manager object definition
notification = NotificationManager()

# 1. Update IATA Code of destination cities
# 2. Extract lowest flight price for destination cities
for each_city in sheet_data["prices"]:
    if each_city["iataCode"] == "":
        # Flight search object definition
        flight_search_manager = FlightSearch(city=each_city["city"])
        location_data = flight_search_manager.kiwi_get_location()
        each_city["iataCode"] = location_data["locations"][0]["code"]
        sheet_data_manager.sheety_put_request(each_city["iataCode"], each_city["id"])
    else:
        pass

    # Extract destination city & cheapest flight cost from kiwi API response
    flight_details = flight_data_manager.flight_search_get_request(iata_code=each_city["iataCode"])
    try:
        outbound_date = (flight_details[0]["route"][0]["local_departure"]).split("T")[0]
        inbound_date = (flight_details[0]["route"][1]["local_departure"]).split("T")[0]
    except IndexError:
        print(f"There's no flight for {each_city['iataCode']}")
    else:
        if flight_details:
            if flight_details[0]["price"] < each_city["lowestPrice"]:
                notification.send_message(price=flight_details[0]["price"], dep_city=DEPARTURE_CITY,
                                          dep_ap_iata_code=DEPARTURE_CITY_IATA_CODE, arr_city=each_city["city"],
                                          arr_ap_iata_code=each_city["iataCode"],
                                          outbound_date=outbound_date, inbound_date=inbound_date)
