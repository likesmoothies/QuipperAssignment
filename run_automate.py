import Factory.DriverFactory
from Factory.DriverFactory import Driver_Factory
from Factory.PageFactory import  PageObject
from Config import Config

driveObj = Driver_Factory()
ConfigObj = Config()

testObj = driveObj.get_web_driver(ConfigObj.BASE_CMS_URL)
testObj = Factory.PageFactory.PageObject("Login_page", driveObj)
testObj.start()
#driveObj.close()
#driveObj.quit()