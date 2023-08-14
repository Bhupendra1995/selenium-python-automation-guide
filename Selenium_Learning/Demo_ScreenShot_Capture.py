# Screen shots method
# driver.get_full_page_screenshot_as_file('/Screenshots/foo.png')
# driver.save_screenshot('/Screenshots/foo.png')
# element.screenshot('/Screenshots/foo.png')

import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class DemoScreenShot():
    def Screenshot(self):
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service= service)
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        cont_button = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
        #cont_button.screenshot(".\\testImg.png")
        cont_button.click()
        time.sleep(2)
        driver.get_screenshot_as_file("C:\\Python Selenium\\BhuviNewProject\\Screenshots\\TestFUll.png")
        driver.save_screenshot("C:\\Python Selenium\\BhuviNewProject\\Screenshots\\TestFUll1.png")

        driver.quit()

ss = DemoScreenShot()
ss.Screenshot()

