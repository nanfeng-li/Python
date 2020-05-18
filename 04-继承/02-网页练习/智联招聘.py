from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.zhipin.com/?ka=header-home')

driver.find_element_by_xpath('//*[text()="登录"]').click()
#driver.find_element_by_xpath('//*[@href="/c101020100/?query=Java&industry=&position="]').click()
time.sleep(10)

