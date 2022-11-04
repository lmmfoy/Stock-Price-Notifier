from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time


service = Service(r"C:\Users\leafo\Desktop\this&that\setup files\chromedriver.exe")

def get_driver():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    # Disable infobars so that they don't interfere with script 
    options.add_argument("disable-infobars")
    # Start browser as maximized 
    options.add_argument("start-maximized")
    # To avoid issues with browser on Linux
    options.add_argument("disable-dev-shm-usage")
    # In order to give script greater privileges, disable sandbox
    options.add_argument("no-sandbox")
    # Help Selenium to avoid detection from browsers
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
    return driver

def main():
    driver = get_driver()
    time.sleep(2)
    percentage = driver.find_element(by="xpath", value="/html/body/div[2]/div/section[1]/div/div/div[2]/span")
    return float(percentage.text[0:-2])

print(main())
# while True:
#     print(main())
#     time.sleep(3600)