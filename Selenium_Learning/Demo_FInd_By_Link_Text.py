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
        driver.get("https://www.yatra.com/homestays")
        # element = driver.find_element(By.LINK_TEXT,'Yatra for Business')
        element = driver.find_element(By.PARTIAL_LINK_TEXT,'Yatra for')
        action  = ActionChains(driver)
        action.click(on_element=element)
        action.perform()
        time.sleep(2)
        driver.close()

locEle = DemoLocatorsBYIDANDName()
locEle.locatorsByID()
