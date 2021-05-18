import unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("Browser Opened")

    def test_open_chercher_tech(self):
        self.driver.get("https://chercher.tech")
        print("Opening CherCherTech")

    def tearDown(self):
        self.driver.quit()
        print("Browser closed")


if __name__ == "__main__":
    unittest.main()
