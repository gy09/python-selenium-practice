from selenium import webdriver

class Link_element:

    def link_text(self):
        baseurl = "https://letskodeit.teachable.com/"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        link = driver.find_element_by_link_text('Practice')
        if link is not None:
            print("We found the link")
        

        partial_text = driver.find_element_by_partial_link_text("Pract")
        if partial_text is not None:
            print("we found the partial text")


obj = Link_element()
obj.link_text()

