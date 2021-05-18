import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class test(unittest.TestCase):
    def test_Firsttest(self):
        baseurl = "https://www.google.co.in/"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.implicitly_wait(3)

        searchfield = driver.find_element_by_xpath("//input[@name='q']")
        searchfield.send_keys("facebook.com")
        # searchbtn = driver.find_elements(By.XPATH, "//input[@name='btnK']")
        # searchbtn.click()
        driver.close()


obj = test()
obj.test_Firsttest()
