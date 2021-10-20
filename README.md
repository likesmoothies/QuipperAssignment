# QuipperAssignment

## Project Description 

This repository contains a set of files as a base for creating selenium automation with python programming language.

## Requirements and Prerequisites

* [Python version 3.x](https://www.python.org/downloads/)

* [Selenium](https://pypi.org/project/selenium/) package for python

 Use the package manager [pip](https://pip.pypa.io/en/stable/) to install both packages.

```bash
pip install selenium
```

* [adb.exe](https://developer.android.com/studio/releases/platform-tools) that can be called from anywhere ([added to PATH environment variable](https://lifehacker.com/the-easiest-way-to-install-androids-adb-and-fastboot-to-1586992378))
  * Can be checked by opening command prompt and type adb

## Files Description

### ConfigFile.py
A Class used to store configuration and can be used to store user defined variable for a cleaner code. This class is used in DriverFactory.py, 

### Factory/DriverFactory.py
A helper class to produce selenium webdriver. Also, it contains method to adjust target the device.

### Factory/PageFactory.py
A factory that produces test objects for the test scrpt

### Page/Main_Page.py
A base for creating test cases. There are two classes, Page class and WebPage class
  * WebPage class used as a base for selenium test script.


### PageObject/Login_Page.py
A sample test script Login_Page. 

This class/file is extending/inheriting Page class so this object/class/file has all properties/functions that has defined in Page.Main_Page.Page class.

### run_chrome.py 
The main test script
