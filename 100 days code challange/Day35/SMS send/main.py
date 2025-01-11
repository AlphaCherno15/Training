import requests, json, datetime
from twilio.rest import Client
# ---------------------------- For weather API ------------------------------- #
API_KEY = "xxx"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
MY_LAT = 10.00
MY_LON = -10.00
PARAMS = {
    "lat": MY_LAT,
    "lon" :MY_LON,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4,
}
# ---------------------------- For twilio ------------------------------- #
account_sid = 'xxx'
auth_token = 'xxx'
# ---------------------------- get weather report ------------------------------- #
def get_weather():
    weather_response = requests.get(OWM_Endpoint, params=PARAMS)
    weather_response.raise_for_status()
    data = weather_response.json()
    return data
def weather_file():
    try:
        with open("weather_data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        dt = get_weather()
        with open("weather_data.json", "w") as data_file:
            json.dump(dt, data_file, indent=4)
            data = json.load(data_file)
    finally:
        return data
# ---------------------------- filter data ------------------------------- #
weather_data = get_weather()
hour_report = []
for weather in weather_data["list"]:
    hour_report.append(
        { "id": int(weather["weather"][0]["id"]),
        "time": int(weather["dt_txt"].split()[1].replace(":00", "")),
        "temperature":weather["main"]["temp"],
        "feels like": weather["main"]["feels_like"],
        "mainly": weather["weather"][0]["main"],
        "description": weather["weather"][0]["description"],
        "max_temp":weather["main"]["temp_max"],
        "min_temp":weather["main"]["temp_min"],
        }
    )
# ---------------------------- using twilio to send WhatsApp ------------------------------- #
text = (f"Weather report at {hour_report[0]["time"]}:00 H\n"
            f"It's gonna be mainly {hour_report[0]["mainly"]} and it is {hour_report[0]["description"]} at the moment\n"
            f"Temperature of {hour_report[0]["temperature"]} °C and feels like {hour_report[0]["feels like"]} °C\n"
            f"Max temperature of {hour_report[0]["max_temp"]} °C and minimum {hour_report[0]["min_temp"]} °C\n\n"
            f"Weather report at {hour_report[1]["time"]}:00 H\n"
            f"It's gonna be mainly {hour_report[1]["mainly"]} and it is {hour_report[1]["description"]} at the moment\n"
            f"Temperature of {hour_report[1]["temperature"]} °C and feels like {hour_report[1]["feels like"]} °C\n"
            f"Max temperature of {hour_report[1]["max_temp"]} °C and minimum {hour_report[1]["min_temp"]} °C\n\n"
            f"Weather report at {hour_report[2]["time"]}:00 H\n"
            f"It's gonna be mainly {hour_report[2]["mainly"]} and it is {hour_report[2]["description"]} at the moment\n"
            f"Temperature of {hour_report[2]["temperature"]} °C and feels like {hour_report[2]["feels like"]} °C\n"
            f"Max temperature of {hour_report[2]["max_temp"]} °C and minimum {hour_report[2]["min_temp"]} °C\n\n"
            f"Weather report at {hour_report[3]["time"]}:00 H\n"
            f"It's gonna be mainly {hour_report[3]["mainly"]} and it is {hour_report[3]["description"]} at the moment\n"
            f"Temperature of {hour_report[3]["temperature"]} °C and feels like {hour_report[3]["feels like"]} °C\n"
            f"Max temperature of {hour_report[3]["max_temp"]} °C and minimum {hour_report[3]["min_temp"]} °C\n"
            )
def send_zap():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+xxxx',
        body=text,
        to='whatsapp:+xxxx'
    )
# ---------------------------- using twilio to send SMS ------------------------------- #
def send_sms():
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+xxxx",
        body="Rain is not expected",
        to='+xxxx'
    )


# send_zap()
