import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoDropdwon():
    def DropDown(self):
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service= service)
        driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
        dropdown = driver.find_element(By.XPATH,'//select[starts-with(@id,"UserTitle")]')
        dd = Select(dropdown)
        time.sleep(3)
        dd.select_by_index(1)
        time.sleep(3)
        dd.select_by_visible_text("CXO / VP / General Manager")
        time.sleep(3)
        dd.select_by_value("Customer_Service_Manager_ANZ")
        time.sleep(3)
        driver.quit()


checkBoxes = DemoDropdwon()
checkBoxes.DropDown()

