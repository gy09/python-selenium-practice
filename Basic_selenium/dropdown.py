from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time


class dropdown_class:
    def dropdown_method(self):

        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        driver.minimize_window()
        time.sleep(2)
        driver.maximize_window()

        driver.implicitly_wait(5)

        drp_element = driver.find_element(By.XPATH, "//select[@id='carselect']")
        sel = Select(drp_element)
        sel.select_by_index(0)
        time.sleep(2)
        sel.select_by_value("benz")
        time.sleep(2)
        sel.select_by_visible_text("Honda")
        time.sleep(2)

        driver.close()


obj = dropdown_class()
obj.dropdown_method()
