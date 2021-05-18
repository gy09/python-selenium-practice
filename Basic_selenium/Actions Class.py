from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class mouseActions:
    def mouseHover(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.execute_script("window.scrollBy(0,1000)")
        time.sleep(3)

        mousebtn = driver.find_element_by_id("mousehover")
        actions = ActionChains(driver)
        actions.move_to_element(mousebtn).perform()
        time.sleep(3)

        try:

            location = "//div[@class='mouse-hover-content']//a[text()='Top']"
            topbtn = driver.find_element(By.XPATH, location)
            actions.move_to_element(topbtn).click().perform()
            time.sleep(5)
            print("The click action is performed")

        except:

            print("Exception has occured unable to find element")


obj = mouseActions()
obj.mouseHover()
