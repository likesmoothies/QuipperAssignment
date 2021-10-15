from selenium import webdriver

class Driver_Factory:
    def __init__(self):
        pass

    def getWebDriver(self, type="chrome"):

        from selenium import webdriver
        if type == "firefox":
            return webdriver.Firefox()
        else:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            return webdriver.Chrome(options=options)
