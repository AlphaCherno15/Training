import requests as rq, datetime as dt, os

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

# APP_ID = ""
# API_KEY = ""
# HOST_DOMAIN = ""
# In PyCharm, you can add your environment variables under "Edit Configurations".
# If you click on the little symbol to the right under "Environment Variables,
# you will bring up a window where you can add the key-value pairs one by one.
# (you can also copy-paste all the environment variables at the same time).

API_KEY = os.environ.get("API_KEY")
APP_ID = os.environ.get("APP_ID")

os.environ['HOST_DOMAIN'] = "https://trackapi.nutritionix.com"
HOST_DOMAIN = os.environ['HOST_DOMAIN']
headers = {
"x-app-id": f"{APP_ID}",
"x-app-key": f"{API_KEY}"
}
param = {
    "query": input("What Exercise You Just Did: "),
    "weight_kg": 75,
    "height_cm": 174,
    "age": 28,
}
response = rq.post(f"{HOST_DOMAIN}/v2/natural/exercise/", json=param, headers=headers)
result = response.json()

token = ""
auth = bearer_headers = {
"Authorization": f"Bearer {token}"
}
for exercise in result["exercises"]:
    inputs = {
        "página1":{
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    write = rq.post(f"https://api.sheety.co/", json=inputs, headers=auth)
    print(write.text)
