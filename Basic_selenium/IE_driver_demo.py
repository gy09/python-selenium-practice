from selenium import webdriver
import time

class ie_demo:
    def ie_run(self):
        driver = webdriver.Ie(executable_path="C:\\Users\\gaura\\workspace_python\\drivers\\IEDriverServer.exe")
        driver.get("http://www.facebook.com")

obj = ie_demo()
obj.ie_run()
