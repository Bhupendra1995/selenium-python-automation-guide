import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class DemoFindHiddenElements():
    def HiddenElements(self):
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service= service)
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        ele = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(ele)
        driver.find_element(By.XPATH,"//button[normalize-space()='Toggle Hide and Show']").click()
        ele1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(ele1)
        #time.sleep(2)
        driver.close()

    def HiddenElementsYatra(self):
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
        driver.get("https://www.yatra.com/")
        driver.find_element(By.XPATH,"//span[@class='demo-icon icon-hotels']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@class='dflex pax-vol']//div[3]//span[@class='ddSpinnerPlus']").click()
        time.sleep(2)
        ele = driver.find_element(By.XPATH,"//select[@class='ageselect']").is_displayed()
        time.sleep(2)
        print(ele)
        # driver.find_element(By.XPATH,"//div[@class='dflex pax-vol']//div[3]//span[@class='ddSpinnerMinus disabled']").click()
        # ele1 = driver.find_element(By.XPATH, "//select[@class='ageselect']").is_displayed()
        # print(ele1)
        driver.quit()



locEle = DemoFindHiddenElements()
#locEle.HiddenElements()
locEle.HiddenElementsYatra()
