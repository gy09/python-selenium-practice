from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class implicitWaitDemo:
    def iw_Test(self):
        baseurl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.get(baseurl)    
        driver.implicitly_wait(5)

        login_field = driver.find_element_by_xpath(
            "//a[contains(@class,'navbar-link')  and contains(@href,'/sign_in')]")
        login_field.click()

        email_field = driver.find_element(By.XPATH, "//input[@id='user_email']")
        email_field.send_keys("test")

        pw_field = driver.find_element(By.XPATH, "//input[@id='user_password']")
        pw_field.send_keys("test")

        login_btn = driver.find_element(By.XPATH, "//input[contains(@class,'btn;') and contains(@value,'Log In')]")
        login_btn.click()
        driver.quit()


obj = implicitWaitDemo()
obj.iw_Test()
