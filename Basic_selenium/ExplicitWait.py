from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select


class Explicit_Wait_Demo():
    def explicit_wait_method(self):
        baseurl = "http://demo.guru99.com/test/login.html"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        email_field = driver.find_element(By.XPATH, "//input[@id ='email']")
        email_field.send_keys("miniyadav231994@gmail.com")
        pw_field = driver.find_element(By.XPATH, "//input[@id ='passwd']")
        pw_field.send_keys("password")

        submit_btn = driver.find_element(By.XPATH,"//button[@id ='SubmitLogin']")
        submit_btn.click()
        pw_field.location_once_scrolled_into_view

        try:
            wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
            element = wait.until(expected_conditions.presence_of_element_located(By.XPATH, "//a[contains(@class,dropdown-toggle) and contains(text(),'Selenium')]"))
            drp_tab1 = driver.find_element(By.XPATH, "//a[contains(@class,dropdown-toggle) and contains(text(),'Selenium')]")
            select_drp = Select(drp_tab1)
            list_item = select_drp.select_by_visible_text("Guru99 Demo Page")
            list_item.click()
        finally:

            driver.close()
obj = Explicit_Wait_Demo()
obj.explicit_wait_method()


