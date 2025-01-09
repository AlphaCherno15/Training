import requests, datetime, smtplib
MY_LAT = 46.408742
MY_LNG = -63.791374
MY_LAT_UP = round(MY_LAT) + 5
MY_LAT_DOWN = round(MY_LAT) - 5
MY_LNG_UP = round(MY_LAT) + 5
MY_LNG_DOWN = round(MY_LAT) - 5
parameters = {
    "lat" : MY_LAT,
    "lng" : MY_LNG,
    "formatted": 0
}
now = datetime.datetime.now()
h_now = int(now.hour)
my_email = "x"
password = "x"
email_to_send = "x"
text = "Go outside, It may be possible to see the ISS"
def get_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = data["iss_position"]["longitude"]
    latitude = data["iss_position"]["latitude"]
    iss_pos = (latitude, longitude)
    return iss_pos
def sun_time():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    h_sunrise = int(sunrise.split("T")[1].split(":")[0])
    h_sunset = int(sunset.split("T")[1].split(":")[0])
    hours = (h_sunrise, h_sunset)
    return hours

def iss_on_me():
    iss = get_iss()
    if iss[0] in range(MY_LAT_DOWN, MY_LAT_UP) and iss[1] in range(MY_LNG_DOWN, MY_LNG_UP):
        sun_hours = sun_time()
        if h_now not in range(sun_hours[0], sun_hours[1]):
            print("it is time")
            with smtplib.SMTP("smtb.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email, to_addrs=email_to_send, msg=f'Subject: ISS is in range\n\n{text}')
        else:
            print("its not time")
    else:
        print("iss is not in the area")
iss_on_me()

