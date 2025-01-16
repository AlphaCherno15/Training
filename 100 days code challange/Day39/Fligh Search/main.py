#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import flight_search, data_manager, pprint, os, time, datetime as dt, notification_manager

today = dt.datetime.today().strftime("%Y-%m-%d")
fs = flight_search.FlightSearch()
dm = data_manager.DataManager()
sms = notification_manager.NotificationManager()
sheet_data = dm.read()

for flight in sheet_data:
    IATA = fs.airport(flight["city"])
    price = fs.get_flight(flight["iataCode"], today, origin="LON")
    sheet_id = flight["id"]
    if price < flight["lowestPrice"]:
        dm.edit(IATA, price , sheet_id)
        try:
            sms.send(flight["city"], price)
        except:
            print("SMS NOT WORKING")
    time.sleep(2)
# for airport in sheet_data:
#     if airport["iataCode"] == "":
#         dm.edit(fs.airport("Testing"),airport["id"])
#
