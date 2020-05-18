import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")

search_windows = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

all_handles = driver.window_handles

for handle in all_handles:
    if handle != search_windows:
        driver.switch_to.window(handle)
        print(driver.title)
        print(driver.current_window_handle)
        driver.find_element_by_name("userName").send_keys("username")
        driver.find_element_by_name("phone").send_keys("123456")
        time.sleep(2)
        driver.close()

driver.switch_to.window(search_windows)
print(driver.title)
print(driver.current_window_handle)
driver.quit()
