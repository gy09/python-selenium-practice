from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class toggle_radio:

    def toggle_method(self):

        Baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(Baseurl)
        driver.maximize_window()

        driver.implicitly_wait(5)

        bmw_radio = driver.find_element(By.XPATH, "//input[@id='bmwradio']")
        bmw_radio.click()
        # time.sleep(2)

        benz_radio = driver.find_element(By.XPATH, "//input[@id='benzradio']")
        benz_radio.click()
        # time.sleep(2)

        honda_radio = driver.find_element(By.XPATH, "//input[@id='hondaradio']")
        honda_radio.click()
        time.sleep(2)

        # radio_btn = driver.find_element(By.XPATH,"//input[contains(@name,'cars') and contains(@type,'radio')]")

        # for radio in radio_btn:
        #     isradio = radio.is_selected()
        #     if not isradio:
        #         radio.click()
        #         time.sleep(2)

        bmw_check = driver.find_element(By.XPATH,"//input[@id='bmwcheck']")
        bmw_check.click()
        time.sleep(2)

        benz_check = driver.find_element(By.XPATH,"//input[@id='benzcheck']")
        benz_check.click()
        time.sleep(2)

        honda_check = driver.find_element(By.XPATH,"//input[@id='hondacheck']")
        honda_check.click()
        time.sleep(2)

        # check_btn = driver.find_element(By.XPATH,"//input[contains(@name,'cars') and contains(@type,'checkbox')]")
        # for check in check_btn:
        #     isselected = check.is_selected()
        #     if isselected is True:
        #         check.click()
        #         time.sleep(2)

        driver.close()

obj = toggle_radio()
obj.toggle_method()




