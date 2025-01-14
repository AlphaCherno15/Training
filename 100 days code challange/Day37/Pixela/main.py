import requests as rq, datetime as dt
# pixla docs https://docs.pixe.la
LINK = "https://pixe.la/v1/users/alphacherno/graphs/graph1.html"
PIXLA_ENDPOINT = "https://pixe.la/v1/users"
user_params = {
    "token": "khhd2heh3hhkj",
    "username": "alphacherno",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
graph_params = {
        "id":"graph1",
        "name":"Cycling Graph",
        "unit":"Km",
        "type":"float",
        "color":"ajisai",
    }
headers = {
        "X-USER-TOKEN": user_params["token"]
    }
# today = str(dt.datetime.today().date()).replace("-","")

# https://www.w3schools.com/python/python_datetime.asp
today_date = dt.datetime.now().strftime("%Y%m%d")

def create_user():
    pixela_endpoint = PIXLA_ENDPOINT
    user = rq.post(url=pixela_endpoint, json=user_params)
    print(user.text)

def create_graph():
    graph = rq.post(url=f"{PIXLA_ENDPOINT}/{user_params['username']}/graphs", json=graph_params, headers=headers)
    print(graph.text)

def post_pixel(day=today_date, quant="0"):
    pixel_params = {
        "date": day,
        "quantity": quant,
    }
    pixel = rq.post(url=f"{PIXLA_ENDPOINT}/{user_params['username']}/graphs/{graph_params['id']}",
                    json=pixel_params, headers=headers)
    print(pixel.text[0:1])

def update_pixel(day, update):
    pixel_params = {
        "quantity": update,
    }
    pixel = rq.put(url=f"{PIXLA_ENDPOINT}/{user_params['username']}/graphs/{graph_params['id']}/{day}",
                   json=pixel_params, headers=headers)
    print(pixel.text)

def delete_pixel(day):
    pixel = rq.delete(url=f"{PIXLA_ENDPOINT}/{user_params['username']}/graphs/{graph_params['id']}/{day}", headers=headers)
    print(pixel.text)

# post_pixel(quant=input("How my Km did you do today: "))
# update_pixel("20250108", "11.5")
# delete_pixel("20250110")