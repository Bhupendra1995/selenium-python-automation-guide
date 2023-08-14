import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class DemoExplicitWait():
    def ExplicitWait(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://app.hubspot.com/login")
        wait = WebDriverWait(driver,10)

        #wait.until(EC.title_is("HubSpot Login"))
        wait.until(EC.title_contains("Hub"))
        print(driver.title)
        username = wait.until(EC.presence_of_element_located((By.ID,"username")))
        username.send_keys("abc@yahoo.com")
        driver.close()

    def WaitForAlert(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        wait = WebDriverWait(driver, 10)
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
        driver.maximize_window()
        wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='iframeResult']")))
        driver.find_element(By.XPATH,"//button[normalize-space()='Try it']").click()
        alert = wait.until(EC.alert_is_present())
        print(alert.text)
        alert.accept()
        time.sleep(3)
        driver.close()

    def ElementToBeClickable(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://app.hubspot.com/login")
        wait = WebDriverWait(driver, 10)
        sign_up = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,"Sign up")))
        print(sign_up.text)
        sign_up.click()
        username = wait.until(EC.visibility_of_element_located((By.XPATH,"(//input[@id='UIFormControl-2'])[1]")))
        username.send_keys("abc@yahoo.com")
        driver.close()


Dexwait = DemoExplicitWait()
#Dexwait.ExplicitWait()
Dexwait.WaitForAlert()
#Dexwait.ElementToBeClickable()