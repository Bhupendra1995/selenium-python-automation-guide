import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DemoLocatorsBYIDANDName():
    def locatorsByID(self):
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service= service)
        driver.get("https://www.yatra.com/")
        att_value = driver.find_element(By.XPATH,"//div[@id='credit-shellBtnID']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(att_value)
        time.sleep(2)
        driver.close()

locEle = DemoLocatorsBYIDANDName()
locEle.locatorsByID()
