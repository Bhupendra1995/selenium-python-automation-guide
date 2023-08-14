from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service = Service(executable_path="C:\\Python Selenium\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service = service)
driver.get("https:\\www.google.com")
driver.maximize_window()
print(driver.title)
driver.close()