from selenium import webdriver


class class_tag_element:

    def class_tag(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()
        driver.get(baseurl)

        link = driver.find_element_by_class_name('displayed-class')
        link.send_keys("Hello")
        if link is not None:
            print("We found the link")

        tag_text = driver.find_element_by_tag_name("h1")
        if tag_text is not None:
            print("we found the partial text")


obj = class_tag_element()
obj.class_tag()

