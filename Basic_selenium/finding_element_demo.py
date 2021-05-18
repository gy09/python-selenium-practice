from selenium import webdriver


class Find_id_name:

    def findelementidname(self):

        baseurl = "https://www.facebook.com/"
        driver = webdriver.Firefox()
        driver.get(baseurl)
        elementid = driver.find_element_by_id("email")
        if elementid is not None:
            print("we found the web element by ID ")
        elementname = driver.find_element_by_name("email")
        if elementname is not None:
            print("we found web element by name")


obj = Find_id_name()
obj.findelementidname()
