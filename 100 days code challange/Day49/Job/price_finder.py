import time, smtplib, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')
SMTP_ADRESS = os.environ.get('SMTP_ADRESS')

origin = "YYG" # Charllotetown
destination = "FLN" # Florianopolis

port = 587
days = [29,30,1,2,3]
months = [9,9,10,10,10]
year = 2025
price_target = 800

# create departure and return dates based on the days and month Lists
departure_dates = [datetime(year, month, day) for day, month in zip(days, months)]
return_dates = [departure + timedelta(days=14) for departure in departure_dates]

def get_prices(d, r):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver =  webdriver.Chrome(options=chrome_options)
    login_url = "https://www.aircanada.com/home/ca/en/aco/flights"
    # time sleeps to wait the page properly open
    login = driver.get(login_url)
    time.sleep(10)
    # print("here")
    time.sleep(0.3)
    cookies_button = driver.find_element(By.XPATH, value='//*[@id="onetrust-accept-btn-handler"]')
    cookies_button.click()
    time.sleep(0.3)
    selct = driver.find_element(By.XPATH, value='//*[@id="flightsOriginLocationbkmgLocationContainer"]/div')
    time.sleep(0.3)
    selct.click()

    # set origin and destination at the website
    ogn_dst = driver.find_element(By.NAME, value='flightsOriginLocation')
    time.sleep(0.3)
    ogn_dst.send_keys(origin, Keys.TAB, Keys.TAB, destination, Keys.TAB)
    time.sleep(0.3)

    # add 1 adult
    adults = driver.find_element(By.XPATH, value='//*[@id="bkmg-mobile-tablet_selectTravelersMainContainer"]/div')
    adults.click()
    time.sleep(0.3)
    add_adult = driver.find_element(By.XPATH, value='//*[@id="bkmg-mobile-tablet_selectTravelers_addTraveler_ADT"]')
    add_adult.click()
    add_adult.send_keys(Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.TAB, Keys.ENTER)
    time.sleep(0.3)

    # set departure and return dates
    departure_date = driver.find_element(By.XPATH, value='//*[@id="bkmg-mobile-tablet_travelDates-formfield-1"]')
    departure_date.send_keys(d, Keys.TAB, r)
    time.sleep(0.3)
    search_button = driver.find_element(By.XPATH, value='//*[@id="bkmg-mobile-tablet_findButton"]')
    search_button.click()
    time.sleep(10)
    all_prices = []

    # find all prices in economic class
    price_element = driver.find_elements(By.CSS_SELECTOR, 'div.cabin-price-amount.font-size-16.ng-star-inserted')
    for price in price_element:
        valor =price.text.replace("$","").replace(",", "")
        all_prices.append(int(valor))
        # print(valor)
    driver.quit()
    return min(all_prices)

text = ""
send = False

# for dates check flights prices
for departure, return_date in zip(departure_dates, return_dates):
    day_price = get_prices(departure.strftime('%d/%m'), return_date.strftime('%d/%m'))
    if day_price < price_target:
        text += f'Fligh for {departure.strftime('%d/%m')} is ${day_price}'
        send = True
        print(text)

# if flights price is under a target, send an email
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
