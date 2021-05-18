from selenium import webdriver


class B_interact:
    def b_menthod(self):
        baseurl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.get(baseurl)

        driver.minimize_window()

        driver.maximize_window()

        web_title = driver.title
        print("The title of the web page is", web_title)

        url = driver.current_url
        print("The value of the current URL is:", url)

        driver.refresh()

        driver.get("https://google.com")

        driver.back()

        driver.forward()

        #source = driver.page_source
        #print("Source of page is", source)

        driver.close()

        driver.quit()

obj = B_interact()
obj.b_menthod()
