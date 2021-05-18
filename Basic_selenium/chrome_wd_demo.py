from selenium import webdriver
import time


class chrome_demo:

    def chrome_test(self):
        # instantiate the chrome browser
        driver = webdriver.Chrome(executable_path="C:\\Users\\gaura\\workspace_python\\drivers\\chromedriver.exe")
        driver.get("http://www.facebook.com")
        time.sleep(30)


obj = chrome_demo()
obj.chrome_test()
