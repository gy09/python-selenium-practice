from selenium import webdriver
from selenium.webdriver.common.by import By


class multiple_elements:
    def mul_elements(self):

        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        elements_class = driver.find_elements_by_class_name("inputs")
        length1 = len(elements_class)
        if elements_class is not None:
            print("we found one element:" + str(length1))

        elements_tag = driver.find_elements(By.TAG_NAME, "td")
        length2 = len(elements_tag)
        if elements_tag is not None:
            print("we found one element:" + str(length2))


obj = multiple_elements()
obj.mul_elements()
