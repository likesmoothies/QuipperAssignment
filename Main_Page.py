import logging
import Config
import time
import unittest
import pytest


class WebPage(unittest.TestCase):
    def __init__(self, driver, conf=None):
        "CONFIG"
        if conf == None:
            conf = Config.Config()
        self.driver = driver