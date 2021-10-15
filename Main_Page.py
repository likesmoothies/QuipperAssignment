from ConfigFile import  Config
import logging
import ConfigFile
import time
import unittest
import pytest


class WebPage(unittest.TestCase):
    def __init__(self, driver, conf=None):
        "CONFIG"
        super().__init__()
        if conf == None:
            conf == ConfigFile.Config()
        self.driver = driver
        self.conf = conf