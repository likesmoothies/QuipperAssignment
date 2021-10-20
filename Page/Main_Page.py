import time

from ConfigFile import  Config
import logging
import ConfigFile
import functools
import unittest
import pytest
from selenium.webdriver.remote import webelement

class WebPage(unittest.TestCase):
    def __init__(self, driver, conf=None):
        ''''''"CONFIG"''''''
        super().__init__()
        if conf == None:
            conf = ConfigFile.Config()
        self.driver = driver
        self.conf = conf

    def wait(self, type, name):
        '''
        Performs wait, depends on type Supported type: time, element type

        Parameters:
        -----------
        type: str
            wait method: 'time', By
        name: str/int

        Example:
        -----------
        wait('time', timeInSecond)
            wait for timeInSeconds
        wait(by, elementName)
            wait until element is shown (by id, by class name)
        '''
        if type == 'time':
            time.sleep( name )
        else:
            while not self.driver.find_elements( type, name ):
                time.sleep( 1 )


