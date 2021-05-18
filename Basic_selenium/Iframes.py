from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Iframe:
    def IframeSwitch(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(2)

        driver.execute_script("window.scrollBy(0,1200)")

        driver.switch_to.frame("courses-iframe")

        searchbtn = driver.find_element(By.XPATH, "//input[@id='search-courses']")
        searchbtn.send_keys("python")
        time.sleep(2)
        driver.switch_to.default_content()

        driver.execute_script("window.scrollBy(0,-1200)")
        btn = driver.find_element(By.ID, "name")
        btn.send_keys("Test Successful")

        driver.close()

obj = Iframe()
obj.IframeSwitch()

