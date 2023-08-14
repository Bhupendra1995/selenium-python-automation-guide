import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DemoAlerts():
    def AlertsPopups(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")

        # Alerts accepted
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.accept()


        #dismiss alerts
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(2)
        driver.switch_to.alert.dismiss()


        #sendkeys
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        print(driver.switch_to.alert.text)
        time.sleep(2)
        driver.switch_to.alert.send_keys("Bhupendra Rathore")
        driver.switch_to.alert.accept()
        time.sleep(4)


ele = DemoAlerts()
ele.AlertsPopups()