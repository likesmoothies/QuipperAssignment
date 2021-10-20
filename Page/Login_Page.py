from Page.Main_Page import WebPage
from Page.Dashboard_Page import Dashboard_page
import logging


#from Config

class Login_page(WebPage):
    def __init__(self, driver,config = None):
        super().__init__(driver,config)
        self.dashboard = Dashboard_page(driver,config = None)
        self.username_field = "//input[@id='user-name']" #id
        self.password_field = 'password'
        self.login_button = 'login-button'
        self.error_box = "//h3"
        self.button_error = "//button[@class='error-button']"
        self.button_menu = "//button[@id='react-burger-menu-btn']"
        self.title = "//span[contains(text(),'Products')]"
        self.button_logout = "//a[@id='logout_sidebar_link']"
        self.label  = "//h4[contains(text(),'Accepted usernames are:')]"

    def start(self):
        self.openpage(self.conf.BASE_CMS_URL)
        self.dologin( self.conf.Valid_User, self.conf.CMS_PASSWORD )
        self.dashboard.logout()
        self.Do_login_invalid_User(self.conf.Invalid_User, self.conf.CMS_PASSWORD)
        #self.dashboard.logout()



    def openpage(self,url):
        logging.info("matching error message")
        self.driver.get(url)
        return True

    def dologin(self,username,password):
        self.InputUsername(username)
        self.InputPassword(password)
        self.driver.find_element('id', self.login_button).click()
        print("Do login valid User : Passed ")
        #if  self.driver.find_element('xpath', self.title).text == "Products" :


    def Do_login_invalid_User(self,username , password ):
        self.InputUsername(username)
        self.InputPassword(password)
        self.driver.find_element('id', self.login_button).click()
        error_text = self.driver.find_element('xpath', self.error_box).text
        #print("Error Message : " + error_text)
        if error_text == "Epic sadface: Sorry, this user has been locked out.":
            print("Do login Invalid User : Passed ")
            return False


    def dologout(self):
        self.driver.find_element('xpath',self.button_menu).click()
        self.driver.find_element('xpath',self.button_logout).is_enabled()
        self.driver.find_element('xpath',self.button_logout).click()
        print("logout Success")
        return True

    def InputUsername(self,usernames):
      self.driver.find_element('xpath',self.username_field).send_keys(usernames)
      print("Username input")
      return  True

    def InputPassword(self,passwords):
        self.driver.find_element('id',self.password_field).send_keys(passwords)
        print("Password input")
        return  True



