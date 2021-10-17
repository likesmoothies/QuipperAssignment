from Main_Page import WebPage
import logging
import pytest


#from Config

class Login_page(WebPage):
    def __init__(self, driver,config = None):
        super().__init__(driver,config)
        self.username_field = "//input[@id='user-name']" #id
        self.password_field = 'password'
        self.login_button = 'login-button'
        self.error_box = 'error-message-container error'
        self.button_error = "//button[@class='error-button']"
        self.button_menu = "//button[@id='react-burger-menu-btn']"
        self.button_logout = "//a[@id='logout_sidebar_link']"
        self.label  = "//h4[contains(text(),'Accepted usernames are:')]"

    #def start(self):
     #   self.openpage()
      #  self.InputPassword()

    def openpage(self,url):
        logging.info("matching error message")
        self.driver.get(url)
        return True
    '''    label = self.driver.find_element('xpath',self.label).text
        print(label)
        self.assertEqual(label,"Accepted usernames are:")
        self.dologin(self.conf.USERNAME_1,self.conf.CMS_PASSWORD)
        self.dologout()'''
        


    def dologin(self,username,password):
        self.InputUsername(username)
        self.InputPassword(password)
        self.driver.find_element('id', self.login_button).click()
        print("success")
        return  True

    def dologout(self):
        self.driver.find_element('xpath',self.button_menu).click()
        self.driver.find_element('xpath',self.button_logout).click()
        print("success")
        return True

    def InputUsername(self,usernames):
      self.driver.find_element('xpath',self.username_field).send_keys(usernames)
      print("Username input")
      return  True

    def InputPassword(self,passwords):
        self.driver.find_element('id',self.password_field).send_keys(passwords)
        print("Password input")
        return  True



