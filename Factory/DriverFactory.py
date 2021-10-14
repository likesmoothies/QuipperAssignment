from selenium import webdriver

class Driver_Factory:

    def __init__(self):
        pass

    def get_web_driver(self, type="chrome"):

        from selenium import webdriver
        if type == "firefox":
            return webdriver.Firefox()
        else:
            return webdriver.Chrome()
