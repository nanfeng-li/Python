# -*- coding: utf-8 -*-
from appium import webdriver
desired_caps = {
        'platformName': 'Android',
        'deviceName': 'bbcbb5d2',
        'platformVersion': '8.0',
        'appPackage': 'com.oneplus.note',
        'appActivity': 'com.oneplus.note.ui.MainActivity'
    }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id('com.oneplus.note:id/list_view').click()