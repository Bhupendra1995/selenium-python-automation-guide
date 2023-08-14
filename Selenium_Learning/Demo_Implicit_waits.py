import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DemoImplicitWaits():
    def ImplicitWaits(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        driver.get("https://secure.yatra.com/social/common/yatra/register")
        driver.maximize_window()
        driver.find_element(By.XPATH,"//input[@id='login-input']").send_keys("abc@yahoo.com")


imp_Wait = DemoImplicitWaits()
imp_Wait.ImplicitWaits()
