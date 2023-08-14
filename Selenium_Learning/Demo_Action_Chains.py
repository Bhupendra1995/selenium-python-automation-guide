import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DemoActionChainsMethods():
    def MouseOver(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        achains = ActionChains(driver)
        #time.sleep(2)
        my_account = driver.find_element(By.XPATH,"//a[contains(text(),'My Account')]")
        achains.move_to_element(my_account).perform()
        #time.sleep(2)
        driver.find_element(By.XPATH,"//a[@id='signInBtn']").click()
        #time.sleep(2)
        driver.back()
        #time.sleep(3)
        more_ele = driver.find_element(By.XPATH, "//span[@class='more-arr']")
        achains.move_to_element(more_ele).perform()
        #time.sleep(3)
        driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
        #time.sleep(3)
        driver.back()
        driver.close()

    def DoubleClick(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        achains = ActionChains(driver)
        time.sleep(2)
        dclick_ele = driver.find_element(By.XPATH,"//p[@ondblclick='myFunction()']")
        achains.double_click(dclick_ele).perform()
        time.sleep(2)

    def RightClick(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_oncontextmenu_html")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        achains = ActionChains(driver)
        time.sleep(2)
        rightClick_ele = driver.find_element(By.CSS_SELECTOR,"div[id='div01'] p")
        achains.context_click(rightClick_ele).perform()
        time.sleep(2)

    def DragAndDrop(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        ele1 = driver.find_element(By.ID,"draggable")
        ele2 = driver.find_element(By.ID,"droppable")
        #ActionChains(driver).drag_and_drop(ele1,ele2).perform()
        ActionChains(driver).drag_and_drop_by_offset(ele1, 100,150).perform()
        time.sleep(2)

    def Sliders(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.snapdeal.com/search?keyword=mobiles&sort=rlvncy")
        driver.maximize_window()
        time.sleep(2)
        ele1 = driver.find_element(By.XPATH,'//a[contains(@class,"left-handle")]')
        ele2 = driver.find_element(By.XPATH,'//a[contains(@class,"right-handle")]')
        ActionChains(driver).drag_and_drop_by_offset(ele1,80,0).perform()
        time.sleep(2)
        ActionChains(driver).drag_and_drop_by_offset(ele2,-40,0).perform()
        #ActionChains(driver).click_and_hold(ele1).pause(1).move_by_offset(60,0).release().perform()
        #ActionChains(driver).move_to_element(ele1).click_and_hold(ele1).pause(1).move_by_offset(50,0).release().perform()
        time.sleep(2)


obj = DemoActionChainsMethods()
obj.MouseOver()
#obj.DoubleClick()
#obj.RightClick()
#obj.DragAndDrop()
#obj.Sliders()