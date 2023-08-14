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
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        elements = driver.find_elements(By.TAG_NAME,'a')
        for i in elements:
            print(i.text)
        #time.sleep(2)
        driver.close()

locEle = DemoLocatorsBYIDANDName()
locEle.locatorsByID()
