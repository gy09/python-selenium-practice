from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Alert:
    def alert_popup(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver =  webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()

        name_field = driver.find_element_by_id("name")
        name_field.send_keys("Gaurav")
        time.sleep(2)

        acceptbtn = driver.find_element(By.ID,"alertbtn")
        acceptbtn.click()
        time.sleep(2)
        alert1 = driver.switch_to.alert
        alert1.accept()

        time.sleep(2)

        name_field.send_keys("Thunder")

        confirmbtn = driver.find_element(By.ID,"confirmbtn")
        confirmbtn.click()
        time.sleep(2)
        alert2 = driver.switch_to.alert
        alert2.dismiss()

obj = Alert()
obj.alert_popup()