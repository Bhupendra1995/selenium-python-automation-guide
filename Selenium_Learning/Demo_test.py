import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DemoAutoSuggest():
    def AutoSuggest(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(15)
        #wait = WebDriverWait(driver,10)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        #time.sleep(5)
        depart_from = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        depart_from.send_keys("New")
        # #time.sleep(3)
        # #result1 = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//div[@class='viewport']//div[1]//li")))
        # result1 = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]//li")
        # for res in result1:
        #     if "New Delhi (DEL)" in res.text:
        #         res.click()
        #         break
        time.sleep(10)
        driver.quit()



checkBoxes = DemoAutoSuggest()
checkBoxes.AutoSuggest()

