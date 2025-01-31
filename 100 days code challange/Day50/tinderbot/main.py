import time, smtplib, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()

login_url = "https://tinder.com"
MY_EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
# SMTP_ADRESS = os.environ.get('SMTP_ADRESS')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
web =  webdriver.Chrome(options=chrome_options)
# time sleeps to wait the page properly open
login = web.get(login_url)
time.sleep(3)
cookies_true = web.find_element(By.XPATH, value='//button[@class="c1p6lbu0 W(100%) W(a)--ml Mx(4px)--ml My(0)--ml" and @data-size="medium"]//div[@class="lxn9zzn" and text()="I accept"]')
cookies_true.click()
time.sleep(0.8)
login_button = web.find_element(By.XPATH, '//a[@href="https://tinder.onelink.me/9K8a/3d4abb81" and @class="c1p6lbu0 Miw(120px)"]//div[@class="lxn9zzn" and text()="Log in"]')
login_button.click()
time.sleep(0.8)
facebook_login = web.find_element(By.XPATH, '//*[@id="u1690640749"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button')
facebook_login.click()
time.sleep(0.8)
base_window = web.window_handles[0]
fb_login_window = web.window_handles[1]
web.switch_to.window(fb_login_window)
time.sleep(1)
facebook_email = web.find_element(By.NAME, 'email')
facebook_email.send_keys(MY_EMAIL, Keys.TAB, PASSWORD, Keys.TAB, Keys.ENTER)
time.sleep(1)
web.switch_to.window(base_window)
