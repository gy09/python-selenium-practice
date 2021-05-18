from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class switch_window:

    def switch_window_method(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseurl)
        driver.maximize_window()
        driver.implicitly_wait(2)

        parentHandle = driver.current_window_handle
        print(parentHandle)

        openWindowBtn = driver.find_element(By.ID, "openwindow")


        openWindowBtn.click()
        time.sleep(3)
        driver.execute_script("window.scroll(0,1000);")
        driver.execute_script("window.scroll(0,-500);")

        time.sleep(3)


        handles = driver.window_handles

        for handle in handles:
            print(handle)

        # win_hieght = driver.execute_script("return window.innerHeight;")
        #
        # print(win_hieght)
        #
        # win_Width = driver.execute_script("return window.innerWidth;")
        #
        # print(win_Width)


obj = switch_window()
obj.switch_window_method()
