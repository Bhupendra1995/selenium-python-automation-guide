import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DemoIFrames():
    def Iframes(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_iframe_target")
        driver.maximize_window()
        # switch to frame by Xpath
        #driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))
        # switch under parent frame by id and class
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.LINK_TEXT,"W3Schools.com").click()
        time.sleep(2)
        # Switch under parent frame pickup first frame by index
        driver.switch_to.frame(0)
        text = driver.find_element(By.TAG_NAME,"h1").text
        time.sleep(2)
        print(text)

dframe = DemoIFrames()
dframe.Iframes()
