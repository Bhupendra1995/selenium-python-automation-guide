import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class DemoMultipleWin():
    def MultipleWin(self):
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()
        time.sleep(2)
        parent = driver.current_window_handle
        driver.find_element(By.XPATH,"//a[normalize-space()='View All']").click()
        time.sleep(2)
        # for handle in all_handel:
        #     if handle != parent:
        #         driver.switch_to.window(handle)
        #         driver.find_element(By.XPATH, "(//span[@class='view-btn flR anim'][normalize-space()='View Details'])[1]").click()
        #         time.sleep(2)
        #         driver.close()
        #         time.sleep(2)
        #         break
        child1 = driver.window_handles[1]
        driver.switch_to.window(child1)
        driver.find_element(By.XPATH,"//ul[@class='wfull noListStyle list']//li[1]//span[1]//span[1]//span[3]//span[1]").click()
        time.sleep(2)
        child2 = driver.window_handles[2]
        driver.switch_to.window(child2)
        time.sleep(2)
        from_dest = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        from_dest.send_keys("New")
        time.sleep(2)
        all_from_dest = driver.find_elements(By.XPATH,"//div[@class='viewport']//li")
        for dest in all_from_dest:
            if "New York (NYC)" in dest.text:
                dest.click()
                time.sleep(2)
                break
        time.sleep(2)
        to_dest = driver.find_element(By.XPATH,"//li[@class='w225']//input[@id='BE_flight_arrival_city']")
        to_dest.send_keys("Agr")
        time.sleep(2)
        all_to_dest = driver.find_elements(By.XPATH,"//div[@class='viewport']//li")
        for dest in all_to_dest:
            if dest.text == "Agra (AGR)":
                dest.click()
                time.sleep(2)
                break
        time.sleep(2)
        driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_date']").click()
        time.sleep(2)
        all_dates = driver.find_elements(By.XPATH,'//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD weekend" and @class!="inActiveTD"]')
        for date in all_dates:
            if date.get_attribute("data-date") == "01/08/2023":
                date.click()
                time.sleep(2)
                break
        time.sleep(2)
        arrival_date = driver.find_element(By.XPATH,"//input[@id='BE_flight_arrival_date']")
        arrival_date.click()
        time.sleep(2)
        all_dates = driver.find_elements(By.XPATH,'//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD weekend" and @class!="inActiveTD" and @class!="weekend"]')
        for date in all_dates:
            if date.get_attribute("data-date") == "02/08/2023":
                date.click()
                time.sleep(2)
                break
        select_pass = driver.find_element(By.XPATH,"//span[@class='flight_cls']")
        select_pass.click()
        driver.find_element(By.XPATH,"//div[@class='iePasenger clearfix']//div[1]//div[1]//div[1]//span[1]").click()
        driver.find_element(By.XPATH,"//div[@class='iePasenger clearfix']//div[2]//div[1]//div[1]//span[1]").click()
        driver.find_element(By.XPATH,"//div[@class='iePasenger clearfix']//div[3]//div[1]//div[1]//span[1]").click()
        time.sleep(4)
        driver.find_element(By.XPATH,"//span[@class='done']").click()
        driver.find_element(By.XPATH,"//input[@id='BE_flight_flsearch_btn']").click()
        time.sleep(4)
        driver.close()
        driver.switch_to.window(child1)
        time.sleep(2)
        driver.close()
        driver.switch_to.window(parent)
        time.sleep(2)
        driver.find_element(By.XPATH,"//span[@class='demo-icon icon-hotels']").click()
        time.sleep(2)
        driver.close()

m_win = DemoMultipleWin()
m_win.MultipleWin()

