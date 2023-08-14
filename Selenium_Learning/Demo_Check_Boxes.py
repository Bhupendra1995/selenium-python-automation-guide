import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class DemoCheckBoxes():
    def CheckBoxes(self):
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service= service)
        driver.get("https://www.ironspider.ca/forms/checkradio.htm")
        driver.find_element(By.XPATH,"//input[@value='red']").click()
        time.sleep(4)
        var1 = driver.find_element(By.XPATH,"//input[@value='red']").is_selected()
        print(var1)
        driver.find_element(By.XPATH, "//input[@value='yellow']").click()
        time.sleep(4)
        var2 = driver.find_element(By.XPATH, "//input[@value='yellow']").is_selected()
        print(var1)
        var3 = driver.find_element(By.XPATH, "//input[@value='blue']").is_selected()
        print(var3)

        driver.quit()


checkBoxes = DemoCheckBoxes()
checkBoxes.CheckBoxes()

