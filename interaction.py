import time
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



def language_selector():
    english_button = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
    english_button.click()

def check_element(element):
    try:
        driver.find_element(By.XPATH, element)
    except:
        return False
    return True


def cookie_click(bool):
    cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
    while bool:
        cookie.click()

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

# time.sleep(5)
# language_selector()
# time.sleep(2)
# cookie = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')

keep_going = True

while keep_going:
    if check_element('//*[@id="langSelect-EN"]'):
        language_selector()
        if check_element('//*[@id="bigCookie"]'):
            cookie_click(True)






# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# # article_count.click()
#
#
# search = driver.find_element(By.NAME, 'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)

