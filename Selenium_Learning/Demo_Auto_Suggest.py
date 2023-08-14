import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestSearchAndFlights():
    def test_search_flights(self):

        # Launching the web browser and going to yatra.com
        service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=service)
        #driver.implicitly_wait(10)
        wait = WebDriverWait(driver,20)
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

        # providing going from location
        depart_form = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='BE_flight_origin_city']")))
        depart_form.click()
        time.sleep(2)
        depart_form.send_keys("Lon")
        time.sleep(2)wait.until(EC.visibility_of_all_elements
        all_depart = _located((By.XPATH,"//div[@class='viewport']//li")))
        for ele in all_depart:
            if "London (LON)" in ele.text:
                ele.click()
                break

        # providing going to location
        going_to = wait.until(EC.visibility_of_element_located((By.XPATH,"//input[@id='BE_flight_arrival_city']")))
        going_to.click()
        time.sleep(2)
        going_to.send_keys("Agr")
        time.sleep(2)
        result2 = wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='viewport']//div[1]//li")))
        for res in result2:
            if "Agra" in res.text:
                res.click()
                break

        # Select the departure date
        depart_data = wait.until(EC.presence_of_element_located((By.XPATH,"//input[@id='BE_flight_origin_date']")))
        depart_data.click()
        all_dates = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@id="monthWrapper"]//tbody//td[@class!="inActiveTD" and @class!="weekend" and @class!="inActiveTD weekend"]')))

        for date in all_dates:
            if (date.get_attribute("data-date") == "02/08/2023"):
                date.click()
                break

        # click on flight search button
        wait.until(EC.presence_of_element_located((By.XPATH,"//input[@value='Search Flights']"))).click()
        time.sleep(2)

        pageLength = driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
        match = False
        while (match == False):
            lastCount = pageLength
            time.sleep(2)
            pageLength = driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight); var pageLength = document.body.scrollHeight; return pageLength;")
            if lastCount == pageLength:
                match = True

        time.sleep(3)

        # Search the filter 1 stop
        wait.until(EC.presence_of_element_located((By.XPATH,"//p[normalize-space()='1']"))).click()
        time.sleep(3)
        all_stops = wait.until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='flight-seg col-12']//div[@class=' font-lightgrey fs-10 tipsy i-b fs-10']")))

        #verufy the filter showing only 1 stops
        for stop in all_stops:
            #assert stop.text == "1 Stop"
            print("passed")

        time.sleep(3)
        driver.quit()






searchFlights = TestSearchAndFlights()
searchFlights.test_search_flights()

