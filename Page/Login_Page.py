from Main_Page import WebPage
import logging
#from Config

class Login_page(WebPage):
    def __init__(self, driver,conf = None):
        super().__init__(driver,conf)
        self.username_field = 'user-name' #id
        self.password_field = 'password'
        self.login_button = 'login-button'
        self.error_box = 'error-message-container error'
        self.button_error = "//button[@class='error-button']"
#        self.

    def openpage(self):
        logging.info("matching error message")
        self.driver.get("https://www.saucedemo.com/")
        logging.info("waiting until username field is shown")

        return  True


