from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.python.org/")

#
# documentation_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
#
#
#
# submit = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
#
# print(submit.text)

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text
    }

print(events)
# price_element = driver.find_element(By.CLASS_NAME, 'a-offscreen')
# price = price_element.get_attribute('innerHTML')
# print(price)
# Keeps the browser open for 10 seconds

driver.quit()

