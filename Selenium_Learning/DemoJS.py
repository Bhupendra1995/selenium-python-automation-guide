import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoJS():
    def Javascript(self):
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service= service)
        #driver.get("https://www.rcvacademy.com/")
        driver.execute_script("window.open('https://www.yatra.com/','_self');")
        time.sleep(8)
        about = driver.execute_script("return document.getElementById('booking_engine_hotels');")
        time.sleep(2)
        driver.execute_script("arguments[0].click();", about)
        time.sleep(4)
        driver.quit()


js = DemoJS()
js.Javascript()


