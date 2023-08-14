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
        driver.get("https://demo.mobiscroll.com/select/multiple-select")
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@id='multiple-select-context']//span[contains(@class,'mbsc-textfield')]").click()
        time.sleep(2)
        dropdown = driver.find_element(By.ID,"multiple-select-select")
        dd = Select(dropdown)
        dd.select_by_index(0)
        dd.select_by_value("2")
        dd.select_by_visible_text("Electronics & Computers")
        dd.select_by_index(3)
        dd.select_by_value("5")
        dd.select_by_visible_text("Toys, Kids & Baby")
        time.sleep(5)
        driver.quit()


checkBoxes = DemoDropdwon()
checkBoxes.DropDown()

