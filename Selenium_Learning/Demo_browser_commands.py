import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


# driver.get("url")
# driver.current_url
# driver.back()
# driver.forward()
# driver.refresh()
# driver.title
# driver.maximize_window()
# driver.minimize_window()
# driver.fullscreen_window()
# driver.close()
# driver.quit()


class DemoBrowserCommands():
    def DemoBrowser(self):
        service = Service(executable_path=GeckoDriverManager().install())
        driver = webdriver.Firefox(service= service)
        driver.get("https://www.bhavnacorp.com/")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        time.sleep(2)
        driver.find_element(By.XPATH,"//a[@id='mainmenu_rptrMenu_ctl00_anchlink']").click()
        time.sleep(4)
        driver.back()
        time.sleep(4)
        driver.forward()
        time.sleep(2)
        driver.quit()

browserCommands = DemoBrowserCommands()
browserCommands.DemoBrowser()
