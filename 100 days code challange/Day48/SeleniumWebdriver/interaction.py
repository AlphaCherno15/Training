from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver =  webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")


# count = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/ul/li[1]/a')
# count = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")
# print(count[0].text)
# count[0].click()

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("python",keys.ENTER)


# test to fill up forms in a webpage
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver =  webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com")

firstName = driver.find_element(By.NAME, value="fName")
firstName.send_keys("Alpha")
lastName = driver.find_element(By.NAME, value="lName")
lastName.send_keys("Cherno")
email = driver.find_element(By.NAME, value="email")
email.send_keys("alphacherno15@gmail.com", Keys.TAB, Keys.ENTER)



# driver.close() #to close a tab
# driver.quit() 