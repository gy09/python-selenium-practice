from selenium import webdriver


class findelement_css_xpath:
    # Baseurl = "https://facebook.com"
    # driver = webdriver.Chrome()
    # driver.get(Baseurl)

    def Findelement_css(self):
        Baseurl = "https://facebook.com"
        driver = webdriver.Chrome()
        driver.get(Baseurl)
        css = driver.find_element_by_css_selector("#email")
        if css is not None:
            print("found the element by css")

        xpath = driver.find_element_by_Xpath("//*[@id='email']")
        if xpath is not None:
            print("Found element by Xpath")


obj = findelement_css_xpath()
obj.Findelement_css()
