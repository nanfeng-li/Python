# -*- coding: utf-8 -*-
from appium import webdriver
desired_caps = {
        'platformName': 'Android',
        'deviceName': 'bbcbb5d2',
        'platformVersion': '8.0',
        'appPackage': 'cn.xuexi.android',
        'appActivity': 'com.alibaba.android.rimet.biz.home.activity.HomeActivity'
    }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id('com.oneplus.calculator:id/digit_9').click()