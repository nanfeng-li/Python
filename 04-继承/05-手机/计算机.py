# -*- coding: utf-8 -*-
from appium import webdriver
desired_caps = {
        'platformName': 'Android',
        'deviceName': 'bbcbb5d2',
        'platformVersion': '8.0',
        'appPackage': 'com.oneplus.calculator',
        'appActivity': 'com.oneplus.calculator.Calculator'
    }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id('com.oneplus.calculator:id/digit_9').click()
driver.find_element_by_id('com.oneplus.calculator:id/op_add').click()
driver.find_element_by_id('com.oneplus.calculator:id/digit_9').click()
driver.find_element_by_id('com.oneplus.calculator:id/eq').click()
