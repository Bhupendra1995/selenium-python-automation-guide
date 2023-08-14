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
        driver.get("https://training.openspan.com/login")
        username = driver.find_element(By.XPATH,"//input[@id='user_name']").send_keys("abc@yahooo.com")
        password = driver.find_element(By.XPATH,"//input[@id='user_pass']").send_keys("Demo123")
        eleState = driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(eleState)
        #time.sleep(2)
        driver.close()

locEle = DemoLocatorsBYIDANDName()
locEle.locatorsByID()
