from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class attribute_text:
    def attribute_text_method(self):

        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(5)

        element = driver.find_element(By.XPATH,"//a[@id ='opentab']")

        text_result = element.text
        att_result = element.get_attribute("class")

        print("The text on the button" , text_result)
        print("Value of the Attribut:" , att_result)

        time.sleep(2)
        driver.close()

obj = attribute_text()
obj.attribute_text_method()
