from ConfigFile import  Config
import logging
import ConfigFile
import functools
import unittest
import pytest
from selenium.webdriver.remote import webelement

class WebPage():
    def __init__(self, driver, conf=None):
        ''''''"CONFIG"''''''
        super().__init__()
        if conf == None:
            conf = ConfigFile.Config()
        self.driver = driver
        self.conf = conf


