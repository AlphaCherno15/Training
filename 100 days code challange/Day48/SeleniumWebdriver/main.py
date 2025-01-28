from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time as t
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver =  webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

timeout = 5 
five_min = 5 * 60
cookie = driver.find_element(By.CSS_SELECTOR, value='#cookie')
stores = driver.find_elements(By.CSS_SELECTOR, value='#store div')
store_ids = [store.get_attribute("id") for store in stores]

all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")

prices = []
for price in all_prices:
    try:
        valor = int(price.text.split()[::-1][0].replace(",", ""))
    except IndexError:
        continue
    else:
        prices.append(valor)

upgrades = dict(zip(store_ids, prices))

def reset_timer():
    global time
    time = t.time()
def reset_timer5():
    global five_min_check
    five_min_check = t.time()
time = t.time()
five_min_check = t.time()
while True:
    # t.sleep(0.001)
    cookie.click()
    available_upgrade = {}
    if t.time() > time + timeout:
        cookie_amount = driver.find_element(By.CSS_SELECTOR, value='#money')
        money = cookie_amount.text.replace(",","")
        # print(money)
        for items in upgrades.items():
            if int(money) > items[1]:
                available_upgrade[items[1]] = items[0]
        max_upgrade = max(available_upgrade)
        buy = available_upgrade[max_upgrade]
        try:
            store = driver.find_element(By.CSS_SELECTOR, value=f'#{buy}').click()
        except Exception as e:
            print(e)
        reset_timer()
    if t.time() > five_min_check + five_min:
        cps = driver.find_element(By.CSS_SELECTOR, value='#cps')
        reset_timer5()
        print(cps.text)
       
