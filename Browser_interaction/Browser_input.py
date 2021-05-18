from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class input_browser:
    def click_send_method(self):
        baseurl ="http://demo.guru99.com/test/selenium-xpath.html"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        user_id = driver.find_element(By.XPATH, "//input[@name='uid']")
        user_id.send_keys("gaurav")

        pw_id = driver.find_element(By.XPATH, "//input[@name='password']")
        pw_id.send_keys("Naruto123")

        time.sleep(10)
        reset_btn = driver.find_element(By.XPATH,"//input[@type='reset']")
        reset_btn.click()

        driver.close()

obj = input_browser()
obj.click_send_method()
