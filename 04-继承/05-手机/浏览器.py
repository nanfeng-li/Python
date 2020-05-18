#coding=utf-8
from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '8.0'
desired_caps['deviceName'] = '52ec8347'

desired_caps['appPackage'] = 'com.android.browser'
desired_caps['appActivity'] = 'com.tencent.mtt.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_name("2").click()
driver.find_element_by_name("0").click()
driver.find_element_by_name("1").click()
driver.find_element_by_name("8").click()
driver.quit()
