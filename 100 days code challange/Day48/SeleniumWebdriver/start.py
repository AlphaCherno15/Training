import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# selenium documentation https://selenium-python.readthedocs.io
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver =  webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price =  driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(price.text)

# test2 = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/time')
# print(test2.text)

# create a dictc wiht elements in the website

# events = {}
# n = 1
# for event in range(0,4):
#     event_date = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{n}]/time')
#     event_link = driver.find_element(By.XPATH, value=f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{n}]/a')
#     events[n] = {"time":f'2025-{event_date.text}',
#                     "name":event_link.text
#                     }
#     n += 1
# print(events)


# teacher solution
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {index + 1:{f'2025-{event_times[index].text}':event_names[index].text} for index in range(len(event_times))}
print(events)
# driver.close() #to close a tab
driver.quit() #to close the web window

