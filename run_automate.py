import logging

from Factory.DriverFactory import Driver_Factory
from Factory.PageFactory import  PageObject
from ConfigFile import Config

driveObj = Driver_Factory()
ConfigObj = Config()

webdriver = driveObj.getWebDriver("firefox")
webdriver.set_window_size(1920,1080)

testObj = PageObject("Login_page", webdriver, ConfigObj)
#testObj.
logging.info("test")
testObj.openpage()
webdriver.close()
#webdriver.quit()