import smtplib, requests, os, json
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')
SMTP_ADRESS = os.environ.get('SMTP_ADRESS')
port = 587

# https://httpbin.org/headers
# https://myhttpheader.com
headers1 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "max-age=0",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": "\"Chromium\";v=\"130\", \"Opera\";v=\"115\", \"Not?A_Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0",
  }

headers2 ={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
        }

text = ""
send = False

def get_price(link, store):
    
    if store == "amazon":
        response = requests.get(link, headers=headers1)
        soup = BeautifulSoup(response.content, 'html.parser')
        price = soup.find(name='span', class_='a-offscreen').getText()
        result = float(price.replace('$', ''))

    elif store == "wayfiar":
        session = requests.Session()
        response = session.get(link, headers=headers2)
        soup = BeautifulSoup(response.text, "lxml")
        price = soup.find(name='span', class_="_1fat8tg5h_1fat8tg2f_1fat8tg13e_1fat8tg174_1fat8tgbl")
        result = response.text
        pass
    return result

with open("amazon_price_tracker/items.json", "r") as file:
    list = json.load(file)

for item in list:
    price = get_price(list[item]["url"], list[item]["store"] )
    if price < list[item]["price"]:
        text += f'The price of the {item} is now ${price}! Buy now! {list[item]["url"]}\n\n'
        send = True
    print(text)

if send:
    print('Sending email...')
    with smtplib.SMTP(SMTP_ADRESS, port) as connection:
         # connection.ehlo()
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="alphacherno15@gmail.com",
            msg=f"Subject:Price Alert!\n\n{text}")

