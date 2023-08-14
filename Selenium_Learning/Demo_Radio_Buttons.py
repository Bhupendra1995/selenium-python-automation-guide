import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class DemoRadioButtons():
    def RadioButtons(self):
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service= service)
        driver.get("https://www.keynotesupport.com/internet/web-contact-form-example-radio-buttons.shtml")
        print(driver.find_element(By.XPATH,"//input[@value='Excel']").is_selected())
        time.sleep(4)
        driver.find_element(By.XPATH,"//input[@value='Excel']").click()
        print(driver.find_element(By.XPATH, "//input[@value='Excel']").is_selected())
        time.sleep(4)
        driver.find_element(By.XPATH, "//input[@value='QBP']").click()
        print(driver.find_element(By.XPATH, "//input[@value='Excel']").is_selected())
        print(driver.find_element(By.XPATH, "//input[@value='QBP']").is_selected())
        driver.quit()


checkBoxes = DemoRadioButtons()
checkBoxes.RadioButtons()

