from selenium import webdriver


class Run_test:
    def run_code(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\gaura\\workspace_python\\drivers\\geckodriver.exe")
        driver.get("http://facebook.com")


obj = Run_test()
obj.run_code()
