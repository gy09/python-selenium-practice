from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Window_Switch:
    def window_Switch_Method(self):
        base_Url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(base_Url)
        driver.maximize_window()
        driver.implicitly_wait(3)

        parentHandle = driver.current_window_handle
        Windowbtn = driver.find_element_by_id("openwindow")
        Windowbtn.click()

        handles = driver.window_handles
        for handle in handles:
            if handle not in parentHandle:
                try:
                    searchfld = driver.find_element(By.XPATH, "//input[@id='search-courses']")
                    searchfld.send_keys("Python")
                    searchbtn = driver.find_element(By.ID, "search-course-button")
                    searchbtn.click()
                except:
                    print("Unable to find the element =")
            break
        time.sleep(3)
        
        driver.switch_to_window(parentHandle)
        Windowbtn.click()


        time.sleep(3)


obj = Window_Switch()
obj.window_Switch_Method()
