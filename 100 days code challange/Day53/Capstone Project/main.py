import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def fill_form(add, rent, url):
    time.sleep(1)
    form_adress = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    form_adress.send_keys(add, Keys.TAB, rent, Keys.TAB, url, Keys.TAB, Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()

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
main_link = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(main_link, headers=headers1)
soup = BeautifulSoup(response.content, 'html.parser')
price = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')
adresses = soup.find_all('address', {'data-test': 'property-card-addr'})
place_link = soup.find_all('a', {'data-test': 'property-card-link'})

filtered_prices = [valor.text.replace("+", "-").replace("/", "-").split("-")[0] for valor in price]
adress_list = [adress.text.strip() for adress in adresses]
link_list = [link.get("href") for link in place_link]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSeEI7o94v2mDOEqWsXnxJAelfaa0AjL5vwYEfT6gmBUMEU1xg/viewform?usp=header")

time.sleep(4)
for i in range(len(place_link)):
    time.sleep(0.5)
    try:
        fill_form(adress_list[i], filtered_prices[i], link_list[i])
    except IndexError:
        continue

driver.quit()