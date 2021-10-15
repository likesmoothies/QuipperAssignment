import logging

from Factory.DriverFactory import Driver_Factory
from Factory.PageFactory import  PageObject
from ConfigFile import Config

driveObj = Driver_Factory()
ConfigObj = Config()

webdriver = driveObj.getWebDriver("chrome")
webdriver.set_window_size(1000,1047)

testObj = PageObject("Login_page", webdriver)
#testObj.
logging.info("test")
testObj.openpage()
#driveObj.close()
#driveObj.quit()