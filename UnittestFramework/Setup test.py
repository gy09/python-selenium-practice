import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_Firsttest(self):
        baseurl = "https://www.google.co.in/"
        self.driver.get(baseurl)
        self.driver.implicitly_wait(3)
        searchfield = self.driver.find_element_by_xpath("//input[@name='q']")
        searchfield.send_keys("facebook")


    def test_Secondtest(self):
        baseurl = "https://www.google.co.in/"
        self.driver.get(baseurl)
        self.driver.implicitly_wait(3)
        searchfield = self.driver.find_element_by_xpath("//input[@name='q']")
        searchfield.send_keys("twitter")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
